from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Area(db.Model):
    __tablename__ = 'areas'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    is_outdoor = db.Column(db.Boolean())
    is_indoor = db.Column(db.Boolean())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='areas', cascade='all, delete')
    spaces = db.relationship('Space', back_populates='area', cascade='all, delete')

class AreaSchema(ma.Schema):
    # Tell Marshmallow to use UserSchema to serialize the 'user' field
    user = fields.Nested('UserSchema', exclude=['password', 'areas', 'spaces'])
    spaces = fields.List(fields.Nested('SpaceSchema', only=['name']))
    name = fields.String(required=True, validate=And(
        Length(min=3, error='Name must be at least 3 characters'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers and spaces are allowed')
    ))
    is_outdoor = fields.Boolean(required=True)
    is_indoor = fields.Boolean(required=True)

    class Meta:
        fields = ('id', 'name', 'is_outdoor', 'is_indoor', 'user', 'spaces')