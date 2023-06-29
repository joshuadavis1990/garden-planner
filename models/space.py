from init import db, ma
from marshmallow import fields

class Space(db.Model):
    __tablename__ = 'spaces'

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))

    area_id = db.Column(db.Integer, db.ForeignKey('areas.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='spaces')

class SpaceSchema(ma.Schema):
    user = fields.Nested('UserSchema', exclude=['password'])

    class Meta:
        fields = ('id', 'name', 'area_id', 'user')