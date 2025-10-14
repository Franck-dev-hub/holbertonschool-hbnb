from flask_restx import Namespace, Resource, fields
from app.services import facade

api = Namespace('users', description='User operations')

# Define the user model for input validation and documentation
user_model = api.model('User', {
    'id': fields.String(
        readonly=True,
        description='The unique identifier of a user'
    ),
    'first_name': fields.String(
        required=True,
        description='First name of the user'
    ),
    'last_name': fields.String(
        required=True,
        description='Last name of the user'
    ),
    'email': fields.String(
        required=True,
        description='Email of the user'
    ),
})


@api.route('/')
class UserList(Resource):
    """
    User Registration and Listing Endpoint
    """
    @api.expect(user_model, validate=True)
    @api.response(201, 'User successfully created')
    @api.response(400, 'Email already registered')
    @api.response(400, 'Invalid input data')
    @api.doc(description="Register a new user")
    def post(self):
        """Register a new user"""
        user_data = api.payload

        # Simulate email uniqueness check
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        # Verify input data
        if (
            user_data['first_name'] == ''
            or user_data['last_name'] == ''
            or user_data['email'] == ''
        ):
            return {'error': 'Invalid input data'}, 400

        # verify email format (simple check)
        if (
            user_data['email'].count('@') != 1
            or '.' not in user_data['email'].split('@')[1]
        ):
            return {'error': 'Invalid input data'}, 400

        new_user = facade.create_user(user_data)
        return {
            'id': new_user.id,
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
        }, 201

    @api.response(200, 'Success')
    @api.doc(description="Get list of users")
    @api.marshal_list_with(user_model)
    def get(self):
        """get list of users"""
        return facade.get_all_users(), 200


@api.route('/<string:user_id>')
class UserUpdateAndFetch(Resource):
    """
    user Update Endpoint
    """
    @api.expect(user_model, validate=True)
    @api.response(200, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.response(400, 'Invalid input data')
    @api.response(400, 'Email already registered')
    def put(self, user_id):
        """
        Put method to update a user's attributes.

        Arguments:
            user_id (str): The ID of the user to update.

        Returns:
            json: A JSON representation of the updated user.
            error: An error message if the user
            is not found or input data is invalid.
        """
        user_data = api.payload

        # Verify user exists
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        user_with_email = facade.get_user_by_email(user_data['email'])
        if user_with_email and user_with_email.id != user_id:
            return {'error': 'Email already registered'}, 400

        # Verify input data
        if (
            user_data.get('first_name') == ''
            or user_data.get('last_name') == ''
            or user_data.get('email') == ''
        ):
            return {'error': 'Invalid input data'}, 400

        # verify email format (simple check)
        if (
            user_data['email'].count('@') != 1
            or '.' not in user_data['email'].split('@')[1]
        ):
            return {'error': 'Invalid input data'}, 400

        facade.update_user(user_id, user_data)
        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 201

    @api.response(200, 'Success')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """
        Get a user by id

        Arguments:
            user_id (str): The ID of the user to retrieve.

        Returns:
            json: A JSON representation of the user.
            error: An error message if the user is not found.
        """
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404

        return {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }, 200
