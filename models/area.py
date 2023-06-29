from init import db, ma
from marshmallow import fields

class Area(db.Model):
    __tablename__ = 'areas'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    is_outdoor = db.Column(db.Boolean())
    is_indoor = db.Column(db.Boolean())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', back_populates='areas', cascade='all, delete')

class AreaSchema(ma.Schema):
    # Tell Marshmallow to use UserSchema to serialize the 'user' field
    user = fields.Nested('UserSchema', exclude=['password', 'areas'])

    class Meta:
        fields = ('id', 'name', 'is_outdoor', 'is_indoor', 'user')