"""
File containing the Amenity class
"""
from app.models.base import BaseModel


class Amenity(BaseModel):
    """
    Class representing an Amenity for a place to stay.
    """
    def __init__(self, name):
        """
        constructor for Amenity class
        """
        super().__init__()
        self.name = name
