from flask import Blueprint
from models.space import Space, SpaceSchema
from init import db

spaces_bp = Blueprint('spaces', __name__, url_prefix='/spaces')

# Get all spaces
@spaces_bp.route('/')
def all_spaces():
    # Select all entries in the Spaces table and return them as a JSON object
    stmt = db.select(Space).order_by(Space.name)
    spaces = db.session.scalars(stmt).all()
    return SpaceSchema(many=True).dump(spaces)

# Get one space
@spaces_bp.route('/<int:space_id>')
def one_space(space_id):
    stmt = db.select(Space).filter_by(id=space_id)
    space = db.session.scalar(stmt)
    if space:
        return SpaceSchema().dump(space)
    else:
        return {'error': 'Space not found'}, 404

# Include routes for showing spaces indoors and outdoors