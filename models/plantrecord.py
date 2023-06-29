from init import db, ma
from marshmallow import fields

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

    class Meta:
        fields = ('id', 'name', 'description', 'preferred_location', 'water_rate', 'fertilisation_rate', 'other_comments', 'user', 'plants')