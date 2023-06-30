from flask import request, Blueprint, abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from datetime import timedelta
from models.user import User, UserSchema
from init import db, bcrypt

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Get all users
@auth_bp.route('/users')
@jwt_required()
def all_users():
    admin_required()
    # Select all entries in the PlantRecord table and return them as a JSON object
    stmt = db.select(User).order_by(User.id)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True, exclude=['password']).dump(users)

# Get one user
@auth_bp.route('/users/<int:user_id>')
@jwt_required()
def one_user(user_id):
    admin_required()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': 'User not found'}, 404

# Delete a user
@auth_bp.route('users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    admin_required()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'User not found'}, 404

@auth_bp.route('/register', methods = ['POST'])
def register():
    try:
        # Parse, sanitise and validate the incoming JSON data via the schema
        user_info = UserSchema().load(request.json)
        # Create a new User model instance with the schema data
        user = User(
            f_name = user_info['f_name'],
            l_name = user_info['l_name'],
            email = user_info['email'],
            password = bcrypt.generate_password_hash(user_info['password']).decode('utf-8')
        )
        
        # Add and commit the new user
        db.session.add(user)
        db.session.commit()

        # Return the new user to the client, excluding the password
        return UserSchema(exclude=['password', 'areas', 'spaces']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409
    
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        stmt = db.select(User).filter_by(email=request.json['email'])
        user = db.session.scalar(stmt)
        if user and bcrypt.check_password_hash(user.password, request.json['password']):
            token = create_access_token(identity=user.id, expires_delta=timedelta(days=1))
            return {'token': token, 'user': UserSchema(exclude=['password', 'spaces', 'areas']).dump(user)}
        else:
            return {'error': 'Invalid email address or password'}, 401
    except KeyError:
        return {'error': 'Email address and password are required'}, 400
    
def admin_required():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401, description='You must be an admin')

def admin_or_owner_required(owner_id):
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not (user and (user.is_admin or user_id == owner_id)):
        abort(401, description='You must be an admin or the owner')