from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('protected', description="JWT Protected route")


@api.route('protected')
class Protected(Resource):
    """
    protected JWT route for testing
    """
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        return {"message": f"{current_user} entered protected"}
