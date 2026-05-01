from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
import os
import time
from urllib.parse import urljoin

def scrape_with_selenium(url, output_dir='portfolio_data'):
    """Scrape using Selenium for JavaScript-rendered content"""
    
    # Setup Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in background
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    driver = webdriver.Chrome(options=options)
    
    try:
        print(f"Loading {url}...")
        driver.get(url)
        
        # Wait for portfolio items to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "project-item")))
        
        # Scroll to load all items
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # Find all portfolio items
        items = driver.find_elements(By.CLASS_NAME, "project-item")
        print(f"Found {len(items)} portfolio items")
        
        portfolio_data = []
        images_dir = os.path.join(output_dir, 'images')
        os.makedirs(images_dir, exist_ok=True)
        
        for idx, item in enumerate(items, 1):
            try:
                # Extract data
                title_elem = item.find_element(By.CLASS_NAME, "project-title")
                title = title_elem.text if title_elem else f"Project_{idx}"
                
                category_elem = item.find_element(By.CLASS_NAME, "project-category")
                category = category_elem.text if category_elem else "Uncategorized"
                
                # Get image
                img_elem = item.find_element(By.TAG_NAME, "img")
                img_url = img_elem.get_attribute('src')
                if img_url:
                    img_url = urljoin(url, img_url)
                
                # Get redirect link
                link_elem = item.find_element(By.TAG_NAME, "a")
                redirect_url = link_elem.get_attribute('href')
                
                # Download image
                if img_url:
                    response = requests.get(img_url)
                    safe_title = title.replace(' ', '_').replace('/', '_')
                    img_path = os.path.join(images_dir, f"{idx:03d}_{safe_title}.jpg")
                    
                    with open(img_path, 'wb') as f:
                        f.write(response.content)
                    print(f"✓ Downloaded: {os.path.basename(img_path)}")
                
                portfolio_data.append({
                    'title': title,
                    'category': category,
                    'image_url': img_url,
                    'redirect_url': redirect_url,
                    'local_path': img_path if img_url else None
                })
                
            except Exception as e:
                print(f"Error processing item {idx}: {e}")
        
        # Save metadata
        metadata = {
            'source_url': url,
            'total_items': len(portfolio_data),
            'scraped_date': time.strftime('%Y-%m-%d %H:%M:%S'),
            'items': portfolio_data
        }
        
        json_path = os.path.join(output_dir, 'portfolio_data.json')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Success! Saved {len(portfolio_data)} items to {output_dir}")
        
    finally:
        driver.quit()
    
    return portfolio_data

# Run the scraper
if __name__ == "__main__":
    # Try BeautifulSoup first
    try:
        from bs4 import BeautifulSoup
        scraper = PortfolioScraper("https://samruddhimeher.netlify.app/")
        data = scraper.scrape_portfolio()
    except Exception as e:
        print(f"BeautifulSoup scraping failed: {e}")
        print("Trying Selenium...")
        data = scrape_with_selenium("https://samruddhimeher.netlify.app/")