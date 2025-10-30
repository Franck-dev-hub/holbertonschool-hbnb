from app.models.base import BaseModel
from app import bcrypt
from app.extensions import db
from sqlalchemy.orm import validates
import re


class User(BaseModel):
    __tablename__ = 'users'

    email = db.Column(db.String(120), nullable=False, unique=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    places = db.relationship('Place', backref="user", lazy=True)
    reviews = db.relationship('Review', backref='user', lazy='select')

    def __init__(self, email, first_name, last_name, password=None, is_admin=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.is_admin = is_admin

        self.password = password
        if password:
            self.hash_password(password)


    def hash_password(self, password: str):
        """Hashes the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password: str) -> bool:
        """Verifies if the provided password matches the hashed password."""
        return bcrypt.check_password_hash(self.password, password)

    def update(self, data: dict):
        """Update user attributes with provided data."""
        allowed_fields = {'email', 'first_name', 'last_name', 'password', 'is_admin'}
        for field, value in data.items():
            if field not in allowed_fields:
                continue

            if field == 'password' and value:
                self.hash_password(value)
            elif field in {'first_name', 'last_name'}:
                setattr(self, field, value.strip())
            else:
                setattr(self, field, value)

    @validates("email")
    def validate_email(self, key, value):
        if not value:
            raise ValueError("Email cannot be empty.")
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not re.match(pattern, value):
            raise ValueError("Invalid email format.")
        return value.lower()

    @validates("first_name", "last_name")
    def validate_name(self, key, value):
        if not value or not value.strip():
            raise ValueError(f"{key.replace('_', ' ').capitalize()} cannot be empty.")
        return value.strip()

    def to_dict(self):
        """Convert the user object to a dictionary."""
        return {
            'id': str(self.id),
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'is_admin': self.is_admin
        }
