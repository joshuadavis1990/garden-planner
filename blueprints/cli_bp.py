from flask import Blueprint
from models.user import User
from models.plantrecord import PlantRecord
from models.plant import Plant
from init import db, bcrypt

cli_bp = Blueprint('db', __name__)

@cli_bp.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')

@cli_bp.cli.command('seed')
def seed_db():
    # Create separate instances of the User model in memory
    users = [
        User(
            f_name = 'Joshua',
            l_name = 'Davis',
            email = '14209@coderacademy.edu.au',
            password = bcrypt.generate_password_hash('coderacademy').decode('utf-8'),
            is_admin = True
        ),
        User(
            f_name = 'Neil',
            l_name = 'Armstrong',
            email = 'neilarmstrong@gmail.com',
            password = bcrypt.generate_password_hash('astronaut').decode('utf-8')
        ),
        User(
            f_name = 'Donald',
            l_name = 'Trump',
            email = 'donaldtrump@gmail.com',
            password = bcrypt.generate_password_hash('makeamericagreat').decode('utf-8')
        )
    ]
    # Create separate instances of the PlantRecords model in memory
    plant_records = [
        PlantRecord(
            name = 'Camellia',
            description = 'Camellias are attrative evergreen shrubs with a variety of flower colours.',
            preferred_location = 'Partial sun',
            water_rate = 'Average',
            fertilisation_rate = 'Key feeding times are autumn as buds are developing and in spring once flowering has finished.',
            other_comments = 'Keep the plant moist but well-drained.'
        ),
        PlantRecord(
            name = 'Pansy',
            description = 'A large-flowered hybrid plant cultivated as a garden flower.',
            preferred_location = 'Partial sun',
            water_rate = 'Average',
            fertilisation_rate = 'Use a controlled release fertiliser when planting.',
            other_comments = 'Keep the plant moist but well-drained.'
        )
    ]
    # Create separate instances of the Plants model in memory
    plants = [
        Plant(
            date_planted = '',
            date_fertilised = '',
        ),
        Plant(
            date_planted = '',
            date_fertilised = ''
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