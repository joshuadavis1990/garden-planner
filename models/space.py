from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

class Space(db.Model):
    # Plural table name
    __tablename__ = 'spaces'

    # Class attributes
    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))

    # Set up foreign key attributes
    # The db.relationship() function provides a relationship between two mapped classes
    area_id = db.Column(db.Integer, db.ForeignKey('areas.id', ondelete='CASCADE'), nullable=False)
    area = db.relationship('Area', back_populates='spaces', cascade='all, delete')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='spaces', cascade='all, delete')

# Create Marshmallow schema to validate and serialize input data so it can be JSONified
class SpaceSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password', 'areas', 'spaces'])
    area = fields.Nested('AreaSchema', only=['name', 'is_outdoor', 'is_indoor'])
    name = fields.String(required=True, validate=Length(min=3))

    class Meta:
        fields = ('id', 'name', 'user', 'area', 'area_id')