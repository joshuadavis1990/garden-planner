from init import db, ma

class Area(db.Model):
    __tablename__ = 'areas'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    is_outdoor = db.Column(db.Boolean())
    is_indoor = db.Column(db.Boolean())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class AreaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'is_outdoor', 'is_indoor', 'user_id')