from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from app.database import db

from config import config
from app.api.v1.places import api as places_ns
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as auth_ns
from app.api.v1.protected import api as protected_ns

# global jwt manager
jwt = JWTManager()


def create_app():
    # initializing app
    app = Flask(__name__)
    api = Api(
        app, version='1.0',
        title='HBnB API',
        description='HBnB Application API',
        doc='/api/v1/'
    )

    # initiaalize the JWTManager
    jwt.init_app(app)

    # initiaalize db
    db.init_app(app)

    # load config
    app.config.from_object(config["development"])

    # Register the users namespace
    api.add_namespace(users_ns, path='/api/v1/users')
    # Register the places namespaces
    api.add_namespace(places_ns, path='/api/v1/places')
    # Register the amenities namespace
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    # Register the reviews namespace
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    # Register the auth namespace
    api.add_namespace(auth_ns, path="/api/v1/auth")
    # import protected route
    api.add_namespace(protected_ns, path="/api/v1/protected")

    return app
