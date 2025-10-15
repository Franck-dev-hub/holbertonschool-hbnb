from app.models.base import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        """Validates that price is a float >= 0, otherwise raises an exception."""
        if not isinstance(value, (float, int)):
            raise ValueError("The price must be a number (float or int)")
        if float(value) < 0:
            raise ValueError("The price must be greater than or equal to 0")
        self._price = float(value)

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        """Validates that the latitude is between -90 and 90."""
        if not isinstance(value, (float, int)):
            raise ValueError("The latitude must be a number (float or int)")
        if float(value) < -90 or float(value) > 90:
            raise ValueError("The latitude must be between -90 and 90")
        self._latitude = float(value)

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        """Validates that the longitude is between -180 and 180."""
        if not isinstance(value, (float, int)):
            raise ValueError("The longitude must be a number (float or int)")
        if float(value) < -180 or float(value) > 180:
            raise ValueError("The longitude must be between -180 and 180")
        self._longitude = float(value)