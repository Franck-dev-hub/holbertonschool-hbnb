"""
File containing the Amenity class
"""
from app.models.base import BaseModel
from app.extensions import db


class Amenity(BaseModel):
    __tablename__ = "amenities"

    name = db.Column(db.String(50), nullable=False)
    """
    Class representing an Amenity for a place to stay.
    """
    def __init__(self, name):
        """
        constructor for Amenity class

        Arguments:
            name (str): the name of the Amenity
        """
        super().__init__()
        self.name = name
