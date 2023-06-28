from flask import Blueprint, request
from models.plant import Plant, PlantSchema
from init import db
from datetime import date

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
    
# Create a new plant
@plants_bp.route('/', methods=['POST'])
def create_plant():
    plant_info = PlantSchema().load(request.json)
    plant = Plant(
        date_planted = date.today(),
        date_fertilised = plant_info['date_fertilised']
    )
    # Add and commit the new plant to the session
    db.session.add(plant)
    db.session.commit()
    # Send the new plant back to the client
    return PlantSchema().dump(plant), 201

# Include routes for showing all indoor and outdoor plants