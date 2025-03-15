from backend.models import User, Image
from .auth import auth_bp
from .images import images_bp

routes = Blueprint("routes", __name__)

# Initialize S3 Client
s3 = boto3.client(
    "s3",
    aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("S3_SECRET_KEY"),
    region_name=os.getenv("S3_REGION"),
)

@routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = User(username=data["username"], email=data["email"])
    user.set_password(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401

@routes.route("/upload", methods=["POST"])
@jwt_required()
def upload():
    user_id = get_jwt_identity()
    file = request.files["file"]
    file_name = file.filename
    s3.upload_fileobj(file, os.getenv("S3_BUCKET"), file_name)
    image = Image(user_id=user_id, file_name=file_name)
    db.session.add(image)
    db.session.commit()
    return jsonify({"message": "File uploaded successfully", "file_name": file_name})

@routes.route("/images", methods=["GET"])
@jwt_required()
def get_images():
    user_id = get_jwt_identity()
    images = Image.query.filter_by(user_id=user_id).all()
    return jsonify([{"file_name": img.file_name} for img in images])
