import os
import re
import shutil

# Directories and files to exclude from searching
EXCLUDE_DIRS = {'.git', 'unused-assests', '__pycache__', 'venv', 'node_modules'}
MEDIA_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.mp4', '.svg', '.webp', '.gif'}

def get_all_media_files(root_dir):
    media_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude directories
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        
        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in MEDIA_EXTENSIONS:
                media_files.append(os.path.join(dirpath, f))
    return media_files

def get_all_code_files(root_dir):
    code_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude directories
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        
        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in {'.html', '.css', '.js', '.json', '.py'} and f != 'cleanup_assets.py':
                code_files.append(os.path.join(dirpath, f))
    return code_files

def extract_references_from_code(code_files):
    references = set()
    for cf in code_files:
        with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            # Find anything that looks like a filename with a media extension
            # This regex looks for word characters, spaces, dashes, underscores, etc. followed by an extension
            matches = re.findall(r'[\w\-\.\/ ]+\.(?:png|jpg|jpeg|mp4|svg|webp|gif)', content, re.IGNORECASE)
            for m in matches:
                # Get the basename (the filename itself) just to be safe
                basename = os.path.basename(m.strip())
                references.add(basename)
                
                # Also add the URL decoded version just in case
                decoded = basename.replace('%20', ' ')
                references.add(decoded)
    return references

def main():
    root_dir = os.getcwd()
    unused_dir = os.path.join(root_dir, 'unused-assests')
    os.makedirs(unused_dir, exist_ok=True)
    
    media_files = get_all_media_files(root_dir)
    code_files = get_all_code_files(root_dir)
    
    references = extract_references_from_code(code_files)
    print(f"Found {len(references)} unique asset references in code.")
    print(f"Found {len(media_files)} total media files in project.")
    
    moved_count = 0
    for mf in media_files:
        basename = os.path.basename(mf)
        # If the exact basename is not in any code file, consider it unused
        if basename not in references:
            # We should also check if it's referenced with some other encoding or path
            # But checking basename is a very safe heuristic
            dest_path = os.path.join(unused_dir, basename)
            
            # Avoid overwriting if multiple files have same name
            if os.path.exists(dest_path):
                base, ext = os.path.splitext(basename)
                dest_path = os.path.join(unused_dir, f"{base}_{moved_count}{ext}")
                
            try:
                shutil.move(mf, dest_path)
                moved_count += 1
                print(f"Moved: {mf} -> {dest_path}")
            except Exception as e:
                print(f"Error moving {mf}: {e}")
                
    print(f"\nCleanup complete. Moved {moved_count} unused files to 'unused-assests' folder.")

if __name__ == '__main__':
    main()
