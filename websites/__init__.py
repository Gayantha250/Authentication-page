import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'fjshfksjdflksjflksjflksjf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from  .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Note
    create_database(app)

    return app

def create_database(app):
    full_path = path.join(os.getcwd(), DB_NAME)
    print("Checking for DB at:", full_path)
    if not os.path.exists(full_path):
        print("DB does not exist. Creating now...")
        with app.app_context():
            db.create_all()
            print("Tables in metadata:", db.metadata.tables)

        print('Database created successfully')
    else:
        print("DB already exists.")
