from os import error
from flask_restx import Namespace, Resource, fields
from jsonschema.validators import validate
from app.services import facade
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(required=True, description='Amenity ID'),
    'name': fields.String(required=True, description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(required=True, description='User ID'),
    'first_name': fields.String(required=True, description='First name of the owner'),
    'last_name': fields.String(required=True, description='Last name of the owner'),
    'email': fields.String(Required=True, description='Email of the owner')
})

# Adding the review model
review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    # 'owner': fields.Nested(user_model, description='Owner of the place'),
    'amenities': fields.List(fields.String(description="Id of amenity"), required=True, description='List of amenities'),
    # 'reviews': fields.List(fields.Nested(review_model), description='List of reviews')
    'rooms': fields.Integer(required=True, description='rooms'),
    'surface': fields.Float(required=True, description='surface'),
    'capacity': fields.Integer(required=True, description='capacity'),
})


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model, validate=True)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload

        existing_user = facade.get_user(place_data["owner_id"])
        if not existing_user:
            return {'error': 'User not found'}, 404

        for amenity in place_data["amenities"]:
            existing_amenity = facade.get_amenity(amenity)
            if not existing_amenity:
                return {'error': 'Amenity not found'}, 404

        if len(place_data["description"]) > 500:
            return {"error": 'Invalid input data'}, 400

        try:
            new_place = facade.create_place(place_data)
        except ValueError:
            return {'error': 'Invalid input data'}, 400

        for amenity in place_data.get("amenities"):
            new_place.add_amenity(facade.get_amenity(amenity))

        return {
            'id': new_place.id,
            'title': new_place.title,
            'description': new_place.description,
            'price': new_place.price,
            'latitude': new_place.latitude,
            'longitude': new_place.longitude,
            'owner_id': new_place.owner_id,
            'rooms': new_place.rooms,
            'capacity': new_place.capacity,
            'surface': new_place.surface,
        }, 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places"""
        place_list = facade.get_all_places()
        places = []

        if len(place_list) == 0:
            return {'error': 'No place found'}, 404

        for place in place_list:
            places.append({
                'id': place.id,
                'title': place.title,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner_id': place.owner_id,
                'rooms': place.rooms,
                'capacity': place.capacity,
                'surface': place.surface,
            })
        return places, 200


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404

        owner = facade.get_user(place.owner_id)

        amenities = [{
            "id": amenity.id,
            "name": amenity.name
        } for amenity in place.amenities]

        if not place:
            return {'error': 'Place not found'}, 404
        return {
            'id': place.id,
            'title': place.title,
            'description': place.description,
            'price': place.price,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'owner': {
                "id": owner.id,
                "first_name": owner.first_name,
                "last_name": owner.last_name,
                "email": owner.email
            },
            'rooms': place.rooms,
            'capacity': place.capacity,
            'surface': place.surface,
            'amenities': amenities
        }, 200

    @api.expect(place_model, validate=True)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    @jwt_required()
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload
    
        current_user = get_jwt_identity()

        # Set is_admin default to False if not exists
        is_admin = current_user.get('is_admin', False)
        user_id = current_user.get('id')

        place = facade.get_place(place_id)
        if not is_admin and place.owner_id != user_id:
            return {'error': 'Unauthorized action'}, 403

        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404

        owner = facade.get_user(place_data["owner_id"])
        if not owner:
            return {'error': 'User not found'}, 404

        if place_data["title"] == "":
            return {'error': 'Invalid input data'}, 400

        if len(place_data["description"]) > 500:
            return {'error': 'Invalid input data'}, 400

        if place_data["price"] < 0:
            return {'error': 'Invalid input data'}, 400

        if place_data["latitude"] < -90 or place_data["latitude"] > 90:
            return {'error': 'Invalid input data'}, 400

        if place_data["longitude"] < -180 or place_data["longitude"] > 180:
            return {'error': 'Invalid inpuit data'}, 400

        if place_data["rooms"] <= 0:
            return {'error': 'Invalid input data'}, 400

        if place_data["surface"] <= 0:
            return {'error': 'Invalid input data'}, 400

        if place_data["capacity"] <= 0:
            return {'error': 'Invalid input data'}, 400

        facade.update_place(place_id, place_data)

        return {'message': 'Place updated successfully'}, 200

@api.route('/<place_id>/reviews')
class PlaceReviewList(Resource):
    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """
        Retrieve all reviews for a specific place
        """
        existing_place = facade.get_place(place_id)
        if not existing_place:
            return {'error': 'Place not found'}, 404

        review_list = facade.get_reviews_by_place(place_id)

        reviews =[]
        for review in review_list:
            reviews.append({
                'id': review.id,
                'title': review.title,
                'text': review.text,
                'rating': review.rating
        })
        return reviews, 200
