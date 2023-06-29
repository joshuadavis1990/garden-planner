from init import db, ma

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    
    date_planted = db.Column(db.Date())
    date_fertilised = db.Column(db.Date())

    space_id = db.Column(db.Integer, db.ForeignKey('spaces.id'), nullable=False)
    plantrecord_id = db.Column(db.Integer, db.ForeignKey('plantrecords.id'), nullable=False)

class PlantSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date_planted', 'date_fertilised', 'space_id', 'plantrecord_id')