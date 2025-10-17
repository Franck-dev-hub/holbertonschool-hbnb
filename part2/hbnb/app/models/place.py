from app.models.base import BaseModel


class Place(BaseModel):
    def __init__(self, title, price, latitude, longitude, owner_id, rooms, description=None, capacity=0, surface=0, amenities=[], reviews=[]):
        super().__init__()
        if title is not None and 0 < len(title) <= 100:
            self.__title = title
        else:
            raise ValueError
        self.description = description
        if price is not None and price >= 0:
            self.__price = price
        else:
            raise ValueError
        if latitude is not None and -90.0 <= latitude <= 90.0:
            self.__latitude = latitude
        else:
            raise ValueError
        if longitude is not None and -180.0 <= longitude <= 180.0:
            self.__longitude = longitude
        else:
            raise ValueError
        if rooms <= 0:
            raise ValueError
        if surface < 0:
            raise ValueError
        if capacity <= 0:
            raise ValueError
        self.owner_id = owner_id
        self.rooms = rooms
        self.capacity = capacity
        self.surface = surface
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        if title is not None and 0 < len(title) <= 100:
            self.__title = title
        else:
            raise ValueError

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price is not None and price >= 0:
            self.__price = price
        else:
            raise ValueError

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        if latitude is not None and -90.0 <= latitude <= 90.0:
            self.__latitude = latitude
        else:
            raise ValueError

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        if longitude is not None and -180.0 <= longitude <= 180.0:
            self.__longitude = longitude
        else:
            raise ValueError
