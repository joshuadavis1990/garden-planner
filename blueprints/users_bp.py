from flask import Blueprint
from models.user import User, UserSchema
from init import db
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

users_bp = Blueprint('users', __name__, url_prefix='/users')

# Get all users
@users_bp.route('/')
@jwt_required()
def all_users():
    admin_required()
    # Select all entries in the PlantRecord table and return them as a JSON object
    stmt = db.select(User).order_by(User.id)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True, exclude=['password']).dump(users)

# Get one user
@users_bp.route('/<int:user_id>')
@jwt_required()
def one_user(user_id):
    admin_required()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': 'User not found'}, 404