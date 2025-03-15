from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from backend.models import Image
from backend.app import db
from backend.utils.s3_utils import upload_to_s3, get_user_images_from_s3
import datetime
import os

images_bp = Blueprint('images', __name__)

@images_bp.route('/upload', methods=['POST'])
@jwt_required()
def upload():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    if file:
        filename = secure_filename(file.filename)
        current_user_id = get_jwt_identity()
        if upload_to_s3(file, filename):
            new_image = Image(filename=filename, user_id=current_user_id)
            db.session.add(new_image)
            db.session.commit()
            return jsonify({'message': 'File uploaded successfully'}), 201
        else:
            return jsonify({'message': 'Error uploading to S3'}), 500

@images_bp.route('/list', methods=['GET'])
@jwt_required()
def list_images():
    current_user_id = get_jwt_identity()
    images = get_user_images_from_s3(current_user_id)
    return jsonify({'images': images}), 200