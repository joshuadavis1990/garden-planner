from flask import Flask, request, abort
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from os import environ
from dotenv import load_dotenv
from models.user import User, UserSchema
from models.plantrecord import PlantRecord, PlantRecordSchema
from init import db, ma, bcrypt, jwt

load_dotenv()

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')

db.init_app(app)
ma.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

def admin_required():
    user_email = get_jwt_identity()
    stmt = db.select(User).filter_by(email=user_email)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401)

@app.errorhandler(401)
def unauthorized(err):
    return {'error': 'You must be an admin'}, 401
        
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

    # Truncate the tables
    db.session.query(User).delete()
    db.session.query(PlantRecord).delete()

    # Add each user to the session (transaction)
    db.session.add_all(users)
    db.session.add_all(plant_records)

    # Commit the users to the database
    db.session.commit()
    print('Models seeded')

@app.route('/register', methods = ['POST'])
def register():
    try:
        # Parse, sanitise and validate the incoming JSON data via the schema
        user_info = UserSchema().load(request.json)
        # Create a new User model instance with the schema data
        user = User(
            f_name = user_info['f_name'],
            l_name = user_info['l_name'],
            email = user_info['email'],
            password = bcrypt.generate_password_hash(user_info['password']).decode('utf-8')
        )
        
        # Add and commit the new user
        db.session.add(user)
        db.session.commit()

        # Return the new user to the client, excluding the password
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Email address already in use'}, 409
    
@app.route('/login', methods=['POST'])
def login():
    try:
        stmt = db.select(User).filter_by(email=request.json['email'])
        user = db.session.scalar(stmt)
        if user and bcrypt.check_password_hash(user.password, request.json['password']):
            token = create_access_token(identity=user.email, expires_delta=timedelta(days=1))
            return {'token': token, 'user': UserSchema(exclude=['password']).dump(user)}
        else:
            return {'error': 'Invalid email address or password'}, 401
    except KeyError:
        return {'error': 'Email address and password are required'}, 400

@app.route('/plantrecords')
@jwt_required()
def all_plant_records():
    admin_required()

    '''Select all entries in the PlantRecord table and return them as a JSON object'''
    stmt = db.select(PlantRecord).order_by(PlantRecord.name)
    plant_records = db.session.scalars(stmt).all()
    return PlantRecordSchema(many=True).dump(plant_records)

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)