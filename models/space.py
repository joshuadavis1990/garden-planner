from init import db, ma

class Space(db.Model):
    __tablename__ = 'spaces'

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(100))

class SpaceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')