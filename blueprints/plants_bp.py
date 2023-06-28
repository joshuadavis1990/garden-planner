from flask import Blueprint
from models.plant import Plant, PlantSchema
from init import db

plants_bp = Blueprint('plants', __name__, url_prefix='/plants')

# Get all plants
@plants_bp.route('/')
def all_plants():
    # Select all entries in the Plants table and return them as a JSON object
    stmt = db.select(Plant).order_by(Plant.date_planted)
    plants = db.session.scalars(stmt).all()
    return PlantSchema(many=True).dump(plants)

# Get one plant
@plants_bp.route('/<int:plant_id>')
def one_plant(plant_id):
    stmt = db.select(Plant).filter_by(id=plant_id)
    plant = db.session.scalar(stmt)
    if plant:
        return PlantSchema().dump(plant)
    else:
        return {'error': 'Plant not found'}, 404