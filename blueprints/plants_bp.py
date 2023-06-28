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