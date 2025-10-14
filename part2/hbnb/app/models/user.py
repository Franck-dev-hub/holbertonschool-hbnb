"""
Class for handling User objects in the HBNB project.
"""
from app.models.base import BaseModel
import json


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

    def to_json(self):
        return json.dumps(self.__dict__)
