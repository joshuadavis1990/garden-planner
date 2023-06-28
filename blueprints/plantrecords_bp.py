from flask import Blueprint, request
from models.plantrecord import PlantRecord, PlantRecordSchema
from init import db
from flask_jwt_extended import jwt_required
from blueprints.auth_bp import admin_required

plantrecords_bp = Blueprint('plantrecords', __name__, url_prefix='/plantrecords')

# Get all plant records
@plantrecords_bp.route('/')
@jwt_required()
def all_plant_records():
    admin_required()

    '''Select all entries in the PlantRecord table and return them as a JSON object'''
    stmt = db.select(PlantRecord).order_by(PlantRecord.name)
    plant_records = db.session.scalars(stmt).all()
    return PlantRecordSchema(many=True).dump(plant_records)

# Get one plant record
@plantrecords_bp.route('/<int:plantrecord_id>')
def one_plantrecord(plantrecord_id):
    stmt = db.select(PlantRecord).filter_by(id=plantrecord_id)
    plant_record = db.session.scalar(stmt)
    if plant_record:
        return PlantRecordSchema().dump(plant_record)
    else:
        return {'error': 'Plant Record not found'}, 404
    
# Create a new plant record
@plantrecords_bp.route('/', methods=['POST'])
def create_plantrecord():
    # Load the incoming POST data via the schema
    plantrecord_info = PlantRecordSchema().load(request.json)
    # Create a new PlantRecord instance from the plantrecord_info
    plantrecord = PlantRecord(
        name = plantrecord_info['name'],
        description = plantrecord_info['description'],
        preferred_location = plantrecord_info['preferred_location'],
        water_rate = plantrecord_info['water_rate'],
        fertilisation_rate = plantrecord_info['fertilisation_rate'],
        other_comments = plantrecord_info['other_comments']
    )
    # Add and commit the new plant record to the session
    db.session.add(plantrecord)
    db.session.commit()
    # Send the new plant record back to the client
    return PlantRecordSchema().dump(plantrecord), 201

# Update a plant record
@plantrecords_bp.route('/<int:plantrecord_id>', methods=['PUT', 'PATCH'])
def update_plantrecord(plantrecord_id):
    stmt = db.select(PlantRecord).filter_by(id=plantrecord_id)
    plant_record = db.session.scalar(stmt)
    plantrecord_info = PlantRecordSchema().load(request.json)
    if plant_record:
        plant_record.name = plantrecord_info.get('name', plant_record.name)
        plant_record.description = plantrecord_info.get('description', plant_record.description)
        plant_record.preferred_location = plantrecord_info.get('preferred_location', plant_record.preferred_location)
        plant_record.water_rate = plantrecord_info.get('water_rate', plant_record.water_rate)
        plant_record.fertilisation_rate = plantrecord_info.get('fertilisation_rate', plant_record.fertilisation_rate)
        plant_record.other_comments = plantrecord_info.get('other_comments', plant_record.other_comments)
        db.session.commit()
        return PlantRecordSchema().dump(plant_record)
    else:
        return {'error': 'Plant Record not found'}, 404