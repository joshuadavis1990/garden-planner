from init import db, ma
from marshmallow import fields

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    
    f_name = db.Column(db.String)
    l_name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    areas = db.relationship('Area', back_populates='user', cascade='all, delete')
    spaces = db.relationship('Space', back_populates='user', cascade='all, delete')
    plantrecords = db.relationship('PlantRecord', back_populates='user', cascade='all, delete')
    plants = db.relationship('Plant', back_populates='user', cascade='all, delete')

class UserSchema(ma.Schema):
    areas = fields.List(fields.Nested('AreaSchema', exclude=['user', 'id', 'is_outdoor', 'is_indoor']))
    spaces = fields.List(fields.Nested('SpaceSchema', exclude=['user', 'id']))


    class Meta:
        fields = ('f_name', 'l_name', 'email', 'password', 'is_admin', 'areas', 'spaces')