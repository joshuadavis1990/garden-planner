from init import db, ma
from marshmallow import fields

class Space(db.Model):
    __tablename__ = 'spaces'

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))

    area_id = db.Column(db.Integer, db.ForeignKey('areas.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='spaces', cascade='all, delete')
    area = db.relationship('Area', back_populates='spaces', cascade='all, delete')

class SpaceSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password', 'areas', 'spaces'])
    area = fields.Nested('AreaSchema', only=['name', 'is_outdoor', 'is_indoor'])

    class Meta:
        fields = ('id', 'name', 'area_id', 'user', 'area')