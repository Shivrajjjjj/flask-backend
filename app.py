from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # Fixed import
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from backend.config import Config  # Correct import
from backend.routes import auth_bp, images_bp  # Ensure these are defined

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)  # Fixed casing
CORS(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(images_bp, url_prefix='/api/images')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)  # Fixed deployment settings
