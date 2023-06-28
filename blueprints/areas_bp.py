from flask import Blueprint
from models.area import Area, AreaSchema
from init import db

areas_bp = Blueprint('areas', __name__, url_prefix='/areas')

# Get all areas
@areas_bp.route('/')
def all_areas():
    # Select all entries in the Areas table and return them as a JSON object
    stmt = db.select(Area).order_by(Area.name)
    areas = db.session.scalars(stmt).all()
    return AreaSchema(many=True).dump(areas)

# Get all outdoor areas
@areas_bp.route('/outdoors')
def all_outdoor_areas():
    stmt = db.select(Area).where(Area.is_outdoor)
    areas = db.session.scalars(stmt).all()
    return AreaSchema(many=True).dump(areas)

# Get all indoor areas
@areas_bp.route('/indoors')
def all_indoor_areas():
    stmt = db.select(Area).where(Area.is_indoor)
    areas = db.session.scalars(stmt).all()
    return AreaSchema(many=True).dump(areas)

# Get one area
@areas_bp.route('/<int:area_id>')
def one_area(area_id):
    stmt = db.select(Area).filter_by(id=area_id)
    area = db.session.scalar(stmt)
    if area:
        return AreaSchema().dump(area)
    else:
        return {'error': 'Area not found'}, 404