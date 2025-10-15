from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True, description="List of amenities ID's")
})

@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""

        place_data = api.payload

        existing_user = facade.get_user(place_data["owner_id"])
        if not existing_user:
            return {'error': 'User not found'}, 404
        
        place_data["owner"] = existing_user

        try:
            new_place = facade.create_place(place_data)
        except ValueError:
            return {'error': 'Invalid input data'}, 400

        for amenity in place_data["amenities"]:
            new_place.add_amenity(facade.get_amenity(amenity["id"]))

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

        places = facade.get_all_places()
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

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""

        place_data = api.payload
        place = facade.get_place(place_id)

        if not place:
            return {'error': 'Place not found'}, 404

        updated_place = facade.update_place(place_id, place_data)
        if not updated_place:
            return {'error': 'Invalid input data'}, 400

        place.amenities = []
        for amenity in place_data["amenities"]:
            place.add_amenity(facade.get_amenity(amenity["id"]))

        return {'message': 'Place updated successfully'}, 200
