from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from backend.config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    CORS(app)
    JWTManager(app)

    from backend.routes.auth import auth_bp
    from backend.routes.images import images_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(images_bp, url_prefix='/api/images')

    return app
