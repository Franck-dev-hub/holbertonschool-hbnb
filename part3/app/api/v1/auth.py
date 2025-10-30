from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.services import facade

api = Namespace('auth', description="Authentication operations")

# Model for input validation
login_model = api.model('Login', {
    'email': fields.String(Required=True, description="User email"),
    'password': fields.String(Required=True, description="User password")
    }
)


@api.route("/login")
class Login(Resource):
    """
    Class providing Authentication routes
    """
    @api.expect(login_model, validate=True)
    @api.response(401, "Invalid credentials")
    @api.response(200, "access_token")
    def post(self):
        """
        Authentication post request
        """
        creadentials = api.payload

        user = facade.get_user_by_email(creadentials['email'])
        if not user or not user.verify_password(creadentials['password']):
            return {'error': 'Invalid credentials'}, 401

        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={"is_admin": user.is_admin}
        )

        return {'access_token': access_token}, 200
