from init import db, ma

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    date_planted = db.Column(db.Date())
    date_fertilised = db.Column(db.Date())

class PlantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_planted', 'date_fertilised')