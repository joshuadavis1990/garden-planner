from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://garden_planner_dev:camellia@localhost:5432/garden_planner'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(100))
    l_name = db.Column(db.String(100))
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class PlantRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Space(db.Model):
    id = db.Column(db.Integer, primary_key=True)

@app.cli.command('create')
def create_db():
    db.create_all()
    print('Tables created successfully')

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)