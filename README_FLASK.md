# Flask Server for RAM Digital Media

This project has been updated with a Flask backend to support clean URLs (e.g., `/portfolio` instead of `/portfolio.html`).

## Project Structure
- `app.py`: The main entry point for the Flask server.
- `routes.py`: Contains the route definitions and clean URL mapping.
- `templates/`: Not used in this specific configuration (Flask is configured to serve from the root).
- `static/`: Not used (Flask is configured to serve static assets from the root).

## How to Run Locally

1. **Install Flask** (if not already installed):
   ```bash
   pip install flask
   ```

2. **Start the Server**:
   ```bash
   python app.py
   ```

3. **Access the Site**:
   - Home: `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/index`
   - About: `http://127.0.0.1:5000/about`
   - Portfolio: `http://127.0.0.1:5000/portfolio`
   - Works: `http://127.0.0.1:5000/works`

## Clean URLs Mapping
| Route | File Served |
|-------|-------------|
| `/` or `/index` | `index.html` |
| `/about` | `about-us-hero.html` |
| `/portfolio` | `portfolio.html` |
| `/works` | `works-by-sam.html` |

Internal links across all HTML files have been updated to use these clean routes.
