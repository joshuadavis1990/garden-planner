from flask import Blueprint
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
    
# # Create a new plant record
# @plantrecords_bp.route('/', methods=['POST'])
# def create_plantrecord():
