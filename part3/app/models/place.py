from app.models.base import BaseModel
from app.extensions import db

# table association for amenities and places
place_amenity = db.Table('place_amenity',
    db.Column('place_id', db.String, db.ForeignKey('places.id'), primary_key=True),
    db.Column('amenity_id', db.String, db.ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel):
    __tablename__ = 'places'

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    owner_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    rooms = db.Column(db.Integer, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    surface = db.Column(db.Float, nullable=False)
    amenities = db.relationship('Amenity', secondary=place_amenity, lazy='subquery',
                                backref=db.backref('place', lazy=True))
    reviews = db.relationship('Review', backref='place', lazy=True)

    def __init__(self, title, price, latitude, longitude, owner_id, rooms, description=None, capacity=0, surface=0):
        super().__init__()
        if not title or len(title) > 100:
            raise ValueError
        if price is None or price < 0:
            raise ValueError
        if latitude is None or not -90 <= latitude <= 90:
            raise ValueError
        if longitude is None or not -180 <= longitude <= 180:
            raise ValueError

        self.title = title
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
        self.owner_id = owner_id
        self.rooms = rooms
        self.capacity = capacity
        self.surface = surface
        self.amenities = []
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
