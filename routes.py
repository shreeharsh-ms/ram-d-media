from flask import render_template, send_from_directory

def setup_routes(app):
    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about-us-hero.html')

    @app.route('/portfolio')
    def portfolio():
        return render_template('portfolio.html')

    @app.route('/works')
    def works():
        return render_template('works-by-sam.html')

    # Serve other files as static
    @app.route('/<path:filename>')
    def serve_static(filename):
        return send_from_directory('public', filename)
