from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://garden_planner_dev:camellia@localhost:5432/garden_planner'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(100))
    l_name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))

class PlantRecord(db.Model):
    __tablename__ = 'plantrecords'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text())
    preferred_location = db.Column(db.String(50))
    water_rate = db.Column(db.String(50))
    fertilisation_rate = db.Column(db.Text())
    other_comments = db.Column(db.Text())

@app.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')

@app.cli.command('seed')
def seed_db():
    # Create separate instances of the User model in memory
    users = [
        User(
            f_name = 'Joshua',
            l_name = 'Davis',
            email = 'joshuadavis1990@me.com',
            password = 'coderacademy'
        ),
        User(
            f_name = 'Neil',
            l_name = 'Armstrong',
            email = 'neilarmstrong@gmail.com',
            password = 'astronaut'
        ),
        User(
            f_name = 'Donald',
            l_name = 'Trump',
            email = 'donaldtrump@gmail.com',
            password = 'makeamericagreat'
        )
    ]
    plant_records = [
        PlantRecord(
            name = 'Camellia',
            description = 'Queens of the winter flowers, Camellias are attrative evergreen shrubs that are highly prized for the beauty of their exquisite blooms, their splendid evergreen foliage and their compact shapely habit.',
            preferred_location = 'Partial sun',
            water_rate = 'Keep the plant moist but well-drained',
            fertilisation_rate = 'Key feeding times are autumn as buds are developing and in spring once flowering has finished and they are about to put on new growth. Feed with things like manure, compost or a Certified Organic fertiliser like Rooster Booster as all will add nutrients and organic matter to the soil.',
            other_comments = None
        )
    ]    
    # Truncate the tables
    db.session.query(User).delete()
    db.session.query(PlantRecord).delete()

    # Add each user to the session (transaction)
    db.session.add_all(users)
    db.session.add_all(plant_records)

    # Commit the users to the database
    db.session.commit()
    print('Models seeded')

@app.cli.command('all_plant_records')
def all_plant_records():
    plant_records = 

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)