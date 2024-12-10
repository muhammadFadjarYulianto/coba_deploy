from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "*"
        ]
    }
})

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)

from app.model import admins, categories, products, articles, comments
from app.routes import *