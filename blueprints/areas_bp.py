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