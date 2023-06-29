from flask import Blueprint, request
from models.plant import Plant, PlantSchema
from init import db
from datetime import date
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

plants_bp = Blueprint('plants', __name__, url_prefix='/plants')

# Get all plants
@plants_bp.route('/')
@jwt_required()
def all_plants():
    # Select all entries in the Plants table and return them as a JSON object
    stmt = db.select(Plant).order_by(Plant.date_planted)
    plants = db.session.scalars(stmt).all()
    return PlantSchema(many=True).dump(plants)

# Get one plant
@plants_bp.route('/<int:plant_id>')
@jwt_required()
def one_plant(plant_id):
    stmt = db.select(Plant).filter_by(id=plant_id)
    plant = db.session.scalar(stmt)
    if plant:
        return PlantSchema().dump(plant)
    else:
        return {'error': 'Plant not found'}, 404
    
# Create a new plant
@plants_bp.route('/', methods=['POST'])
@jwt_required()
def create_plant():
    plant_info = PlantSchema().load(request.json)
    plant = Plant(
        date_planted = date.today(),
        date_fertilised = plant_info['date_fertilised'],
        space_id = plant_info['space_id']
    )
    # Add and commit the new plant to the session
    db.session.add(plant)
    db.session.commit()
    # Send the new plant back to the client
    return PlantSchema().dump(plant), 201

# Update the data for a single plant
@plants_bp.route('/<int:plant_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_plant(plant_id):
    admin_required()
    stmt = db.select(Plant).filter_by(id=plant_id)
    plant = db.session.scalar(stmt)
    plant_info = PlantSchema().load(request.json)
    if plant:
        plant.date_planted = plant_info.get('date_planted', plant.date_planted)
        plant.date_fertilised = plant_info.get('date_fertilised', plant.date_fertilised)
        db.session.commit()
        return PlantSchema().dump(plant)
    else:
        return {'error': 'Plant not found'}, 404
    
# Delete a plant
@plants_bp.route('/<int:plant_id>', methods=['DELETE'])
@jwt_required()
def delete_plant(plant_id):
    admin_required()
    stmt = db.select(Plant).filter_by(id=plant_id)
    plant = db.session.scalar(stmt)
    if plant:
        db.session.delete(plant)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Plant not found'}, 404

# Include routes for showing all indoor and outdoor plants