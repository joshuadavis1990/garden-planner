from init import db, ma

class PlantRecord(db.Model):
    __tablename__ = 'plantrecords'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text())
    preferred_location = db.Column(db.String(50))
    water_rate = db.Column(db.String(50))
    fertilisation_rate = db.Column(db.Text())
    other_comments = db.Column(db.Text())

class PlantRecordSchema(ma.Schema):
    class Meta:
        fields = ('name', 'description', 'preferred_location', 'water_rate', 'fertilisation_rate', 'other_comments')