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

@app.cli.command('create')
def create_db():
    db.drop_all()
    db.create_all()
    print('Tables created successfully')

@app.cli.command('seed')
def seed_db():
    user = User(
        f_name = 'Anakin',
        l_name = 'Skywalker',
        email = 'anakin@skywalker.com',
        password = 'darthvader'
    )

    db.session.query(User).delete()
    db.session.add(user)
    db.session.commit()
    print('Models seeded')

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)