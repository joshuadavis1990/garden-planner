from flask import Blueprint, request
from models.space import Space, SpaceSchema
from init import db
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

spaces_bp = Blueprint('spaces', __name__, url_prefix='/spaces')

# Get all spaces
@spaces_bp.route('/')
@jwt_required()
def all_spaces():
    # Select all entries in the Spaces table and return them as a JSON object
    stmt = db.select(Space).order_by(Space.name)
    spaces = db.session.scalars(stmt).all()
    return SpaceSchema(many=True).dump(spaces)

# Get one space
@spaces_bp.route('/<int:space_id>')
@jwt_required()
def one_space(space_id):
    stmt = db.select(Space).filter_by(id=space_id)
    space = db.session.scalar(stmt)
    if space:
        return SpaceSchema().dump(space)
    else:
        return {'error': 'Space not found'}, 404
    
# Create a new space
@spaces_bp.route('/', methods=['POST'])
@jwt_required()
def create_space():
    # Load the incoming POST data via the schema
    space_info = SpaceSchema().load(request.json)
    # Create a new Space instance from the space_info
    space = Space(
        name = space_info['name']
    )
    # Add and commit the new space to the session
    db.session.add(space)
    db.session.commit()
    # Send the new space back to the client
    return SpaceSchema().dump(space), 201

# Update a space
@spaces_bp.route('/<int:space_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_space(space_id):
    admin_required()
    stmt = db.select(Space).filter_by(id=space_id)
    space = db.session.scalar(stmt)
    space_info = SpaceSchema().load(request.json)
    if space:
        space.name = space_info.get('name', space.name)
        db.session.commit()
        return SpaceSchema().dump(space)
    else:
        return {'error': 'Space not found'}, 404
    
# Delete a space
@spaces_bp.route('/<int:space_id>', methods=['DELETE'])
@jwt_required()
def delete_space(space_id):
    admin_required()
    stmt = db.select(Space).filter_by(id=space_id)
    space = db.session.scalar(stmt)
    if space:
        db.session.delete(space)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Space not found'}, 404

# Include routes for showing spaces indoors and outdoors