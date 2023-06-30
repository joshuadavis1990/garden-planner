from init import db, ma
from marshmallow import fields, validates_schema
from marshmallow.validate import Length, OneOf, ValidationError

VALID_WATERRATES = ['Light', 'Average', 'Heavy', 'Weekly']

class PlantRecord(db.Model):
    __tablename__ = 'plantrecords'

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))
    description = db.Column(db.Text())
    preferred_location = db.Column(db.String(50))
    water_rate = db.Column(db.String(50))
    fertilisation_rate = db.Column(db.Text())
    other_comments = db.Column(db.Text())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    user = db.relationship('User', back_populates='plantrecords', cascade='all, delete')
    plants = db.relationship('Plant', back_populates='plantrecord', cascade='all, delete')

class PlantRecordSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password'])
    plants = fields.List(fields.Nested('PlantSchema', only=['date_planted', 'date_fertilised', 'id', 'space_id']))
    name = fields.String(required=True, validate=Length(min=3))
    description = fields.String(load_default='')
    preferred_location = fields.String(load_default='')
    water_rate = fields.String(load_default=VALID_WATERRATES[1])
    fertilisation_rate = fields.String(load_default='')
    other_comments = fields.String(load_default='')

    @validates_schema()
    def validate_water_rate(self, data, **kwargs):
        water_rate = [x for x in VALID_WATERRATES if x.upper() == data['water_rate'].upper()]
        if len(water_rate) == 0:
            raise ValidationError(f'Water Rate must be one of: {VALID_WATERRATES}')
        data['water_rate'] = water_rate[0]

    class Meta:
        fields = ('id', 'name', 'description', 'preferred_location', 'water_rate', 'fertilisation_rate', 'other_comments', 'user', 'plants')