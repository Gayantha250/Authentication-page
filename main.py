from flask import Flask
from websites.views import views
from websites.auth import auth

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'  # Needed for session, flash, etc.

    # Register Blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

