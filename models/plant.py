from init import db, ma
from marshmallow import fields

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    
    date_planted = db.Column(db.Date())
    date_fertilised = db.Column(db.Date())

    space_id = db.Column(db.Integer, db.ForeignKey('spaces.id', ondelete='CASCADE'), nullable=False)
    plantrecord_id = db.Column(db.Integer, db.ForeignKey('plantrecords.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='plants', cascade='all, delete')
    plantrecord = db.relationship('PlantRecord', back_populates='plants', cascade='all, delete')

class PlantSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password', 'spaces', 'areas'])
    plantrecord = fields.Nested('PlantRecordSchema', only=['name', 'preferred_location', 'water_rate', 'fertilisation_rate', 'other_comments'])
    date_planted = fields.Date(load_default=None)
    date_fertilised = fields.Date(load_default=None)

    class Meta:
        fields = ('id', 'date_planted', 'date_fertilised', 'space_id', 'plantrecord_id', 'user', 'plantrecord', 'user_id')