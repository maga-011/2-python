from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'wdwwfwfwfesfgesedge2'
    
    
    instance_path = os.path.join(os.getcwd(), 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{instance_path}/mydb.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    db.init_app(app)
    login_manager.init_app(app)
    
    
    login_manager.login_view = "login"

    return app
