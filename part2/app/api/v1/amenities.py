"""
Flask RESTful API for managing amenities.
"""
from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('amenities', description='Amenity operations')

# Define the amenity model for input validation and documentation
amenity_model = api.model('Amenity', {
    'name': fields.String(required=True, description='Name of the amenity')
})

# Define the expected output model
amenity_output_model = api.model('AmenityOutput', {
    'id': fields.String(
        readonly=True,
        description='The unique identifier of an amenity'
    ),
    'name': fields.String(
        readonly=True,
        description='Name of the amenity'
    )
})


@api.route('/')
class AmenityList(Resource):
    """
    Class Amenity Registration and Listing Endpoint
    """
    @api.expect(amenity_model)
    @api.response(201, 'Amenity successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """
        Register a new amenity

        Return:
            Json of the newly created amenity
        """
        amenity = api.payload
        if amenity['name'] == '':
            return {'error': 'Invalid input data'}, 400

        created_amenity = facade.create_amenity(amenity)
        return {
            "id": created_amenity.id,
            "name": created_amenity.name
        }, 201

    @api.response(200, 'List of amenities retrieved successfully')
    @api.marshal_list_with(amenity_output_model)
    def get(self):
        """
        Retrieve a list of all amenities

        Returns:
            Json of all amenities
        """
        return facade.get_all_amenities(), 200


@api.route('/<amenity_id>')
class AmenityResource(Resource):
    @api.response(200, 'Amenity details retrieved successfully')
    @api.response(404, 'Amenity not found')
    def get(self, amenity_id):
        """
        Get amenity details by ID

        Arguments:
            amenity_id (str): identifier for amenity object

        Returns:
            json ammenity on success
            404 Amenity not found on errors
        """
        amenity = facade.get_amenity(amenity_id)
        if not amenity:
            return {'error': 'Amenity not found'}, 404

        print(amenity.id)
        return {
            "id": amenity.id,
            "name": amenity.name
        }, 200

    @api.expect(amenity_model)
    @api.response(200, 'Amenity updated successfully')
    @api.response(404, 'Amenity not found')
    @api.response(400, 'Invalid input data')
    def put(self, amenity_id):
        """
        Update an amenity's information

        Arguments:
            amenity_id (str): identifier for amenity

        Returns:
            error 400 empty input
            error 404 Amenity not found
            success 200 Amenity updated
        """
        amenity = api.payload
        if amenity['name'] == '':
            return {'error': 'Invalid input data'}, 400

        if not facade.get_amenity(amenity_id):
            return {'error': 'Amenity not found'}, 404

        facade.update_amenity(amenity_id, amenity)
        return {
            "message": "Amenity updated successfully"
        }, 200
