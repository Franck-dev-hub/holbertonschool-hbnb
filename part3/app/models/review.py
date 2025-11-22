from app.models.base import BaseModel
from app.extensions import db


class Review(BaseModel):
    __tablename__ = "reviews"

    title = db.Column(db.String(255), nullable=True)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey("users.id"), nullable=False)
    place_id = db.Column(db.String, db.ForeignKey("places.id"), nullable=False)

    def __init__(self, text, rating, place_id, user_id):
        super().__init__()
        if not text or len(text.strip()) == 0:
            raise ValueError("Text can't be empty")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        self.text = text
        self.rating = rating
        self.place_id = place_id
        self.user_id = user_id
