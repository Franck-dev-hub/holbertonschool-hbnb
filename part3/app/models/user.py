"""
Class for handling User objects in the HBNB project.
"""
from app.models.base import BaseModel
from app import bcrypt


class User(BaseModel):
    """
    Class User that inherits from BaseModel.
    """

    def __init__(
        self,
        first_name="",
        last_name="",
        email="",
        is_admin=False,
        password=""
    ):
        """
        User class constructor

        Arguments:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email of the user.
            is_admin (bool): Whether the user has admin privileges.
            password (str): The password of the user.
        """
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
        self.password = password

    def hash_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)