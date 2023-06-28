from flask import Flask
from os import environ
from init import db, ma, bcrypt, jwt
from blueprints.cli_bp import cli_bp
from blueprints.auth_bp import auth_bp
from blueprints.plantrecords_bp import plantrecords_bp
from blueprints.plants_bp import plants_bp
from blueprints.areas_bp import areas_bp
from blueprints.spaces_bp import spaces_bp
from blueprints.users_bp import users_bp

# Factory function for creating and configuring an object, 'app', and returning it
def setup():
    app = Flask(__name__)

    app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': 'You must be an admin'}, 401
            
    app.register_blueprint(cli_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(plantrecords_bp)
    app.register_blueprint(plants_bp)
    app.register_blueprint(areas_bp)
    app.register_blueprint(spaces_bp)
    app.register_blueprint(users_bp)

    return app