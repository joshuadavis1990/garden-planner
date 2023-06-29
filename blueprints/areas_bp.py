from flask import Blueprint, request
from models.area import Area, AreaSchema
from init import db
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

areas_bp = Blueprint('areas', __name__, url_prefix='/areas')

# Get all areas
@areas_bp.route('/')
@jwt_required()
def all_areas():
    # Select all entries in the Areas table and return them as a JSON object
    stmt = db.select(Area).order_by(Area.name)
    areas = db.session.scalars(stmt).all()
    return AreaSchema(many=True).dump(areas)

# Get all outdoor areas
@areas_bp.route('/outdoors')
@jwt_required()
def all_outdoor_areas():
    stmt = db.select(Area).where(Area.is_outdoor)
    areas = db.session.scalars(stmt).all()
    return AreaSchema(many=True).dump(areas)

# Get all indoor areas
@areas_bp.route('/indoors')
@jwt_required
def all_indoor_areas():
    stmt = db.select(Area).where(Area.is_indoor)
    areas = db.session.scalars(stmt).all()
    return AreaSchema(many=True).dump(areas)

# Get one area
@areas_bp.route('/<int:area_id>')
@jwt_required()
def one_area(area_id):
    stmt = db.select(Area).filter_by(id=area_id)
    area = db.session.scalar(stmt)
    if area:
        return AreaSchema().dump(area)
    else:
        return {'error': 'Area not found'}, 404
    
# Create a new area
@areas_bp.route('/', methods=['POST'])
@jwt_required()
def create_area():
    # Load the incoming POST data via the schema
    area_info = AreaSchema().load(request.json)
    # Create a new Area instance from the area_info
    area = Area(
        name = area_info['name'],
        is_outdoor = area_info['is_outdoor'],
        is_indoor = area_info['is_indoor'],
        user_id = area_info['user_id']
    )
    # Add and commit the new area to the session
    db.session.add(area)
    db.session.commit()
    # Send the new area back to the client
    return AreaSchema().dump(area), 201

# Update an area
@areas_bp.route('/<int:area_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_area(area_id):
    admin_required()
    stmt = db.select(Area).filter_by(id=area_id)
    area = db.session.scalar(stmt)
    area_info = AreaSchema().load(request.json)
    if area:
        area.name = area_info.get('name', area.name)
        area.is_outdoor = area_info.get('is_outdoor', area.is_outdoor)
        area.is_indoor = area_info.get('is_indoor', area.is_indoor)
        db.session.commit()
        return AreaSchema().dump(area)
    else:
        return {'error': 'Area not found'}, 404

# Delete an area
@areas_bp.route('/<int:area_id>', methods=['DELETE'])
@jwt_required()
def delete_area(area_id):
    admin_required()
    stmt = db.select(Area).filter_by(id=area_id)
    area = db.session.scalar(stmt)
    if area:
        db.session.delete(area)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Area not found'}, 404