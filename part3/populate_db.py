#!/usr/bin/env python3
"""
Script to populate the database with sample data
"""
from app import create_app
from app.extensions import db
from app.models.user import User
from app.models.place import Place
from app.models.amenity import Amenity
from app.models.review import Review


def populate_database():
    """Populate the database with sample data"""
    app = create_app()

    with app.app_context():
        # Create all tables
        print("Creating database tables...")
        db.create_all()

        # Users
        print("Creating users...")
        users_data = [
            {"email": "john.doe@example.com", "first_name": "John", "last_name": "Doe", "password": "password123", "is_admin": False},
            {"email": "jane.smith@example.com", "first_name": "Jane", "last_name": "Smith", "password": "password123", "is_admin": False},
            {"email": "admin@hbnb.com", "first_name": "Admin", "last_name": "User", "password": "admin123", "is_admin": True},
            {"email": "marie.dupont@example.com", "first_name": "Marie", "last_name": "Dupont", "password": "password123", "is_admin": False},
            {"email": "pierre.martin@example.com", "first_name": "Pierre", "last_name": "Martin", "password": "password123", "is_admin": False},
        ]

        users = []
        for u in users_data:
            user = User.query.filter_by(email=u["email"]).first()
            if not user:
                user = User(**u)
                db.session.add(user)
            users.append(user)
        db.session.commit()
        print(f"Created {len(users)} users")

        # Amenities
        print("Creating amenities...")
        amenities_data = ["WiFi", "Kitchen", "Parking", "Pool", "Air Conditioning", "Heating", "Washer", "Dryer", "TV", "Gym", "Breakfast", "Fireplace", "Garden"]
        amenities = []
        for name in amenities_data:
            amenity = Amenity.query.filter_by(name=name).first()
            if not amenity:
                amenity = Amenity(name=name)
                db.session.add(amenity)
            amenities.append(amenity)
        db.session.commit()
        print(f"Created {len(amenities)} amenities")

        # Places
        print("Creating places...")
        places_data = [
            {
                "title": "Cozy Apartment in Paris",
                "description": "Beautiful apartment in the heart of Paris, close to all major attractions. Perfect for couples or solo travelers.",
                "price": 85.0,
                "latitude": 48.8566,
                "longitude": 2.3522,
                "rooms": 2,
                "capacity": 3,
                "surface": 45.0,
                "owner_email": "john.doe@example.com",
                "amenities": ["WiFi", "Kitchen", "Air Conditioning"]
            },
            {
                "title": "Modern Loft in Lyon",
                "description": "Spacious modern loft with stunning city views. Fully equipped kitchen and comfortable living space.",
                "price": 120.0,
                "latitude": 45.7640,
                "longitude": 4.8357,
                "rooms": 3,
                "capacity": 3,
                "surface": 100.0,
                "owner_email": "jane.smith@example.com",
                "amenities": ["WiFi", "Kitchen", "Parking", "TV", "Heating"]
            },
            {
                "title": "Charming Studio in Nice",
                "description": "Small but charming studio a short walk from the beach. Ideal for solo travelers or couples.",
                "price": 60.0,
                "latitude": 43.7102,
                "longitude": 7.2620,
                "rooms": 1,
                "capacity": 2,
                "surface": 28.0,
                "owner_email": "marie.dupont@example.com",
                "amenities": ["WiFi", "TV", "Washer"]
            },
            {
                "title": "Seaside Villa in Bordeaux",
                "description": "Beautiful villa with garden and pool, perfect for families. Close to vineyards and the coastline.",
                "price": 250.0,
                "latitude": 44.8378,
                "longitude": -0.5792,
                "rooms": 4,
                "capacity": 8,
                "surface": 220.0,
                "owner_email": "pierre.martin@example.com",
                "amenities": ["Pool", "Garden", "Parking", "Air Conditioning"]
            },
            {
                "title": "Central Apartment in Marseille",
                "description": "Bright apartment in the city center with easy access to public transport and restaurants.",
                "price": 95.0,
                "latitude": 43.2965,
                "longitude": 5.3698,
                "rooms": 2,
                "capacity": 4,
                "surface": 55.0,
                "owner_email": "admin@hbnb.com",
                "amenities": ["WiFi", "Kitchen", "Heating"]
            },
            {
                "title": "Countryside Cottage",
                "description": "Cozy cottage surrounded by nature. Fireplace and breakfast included.",
                "price": 110.0,
                "latitude": 46.2276,
                "longitude": 2.2137,
                "rooms": 3,
                "capacity": 5,
                "surface": 90.0,
                "owner_email": "john.doe@example.com",
                "amenities": ["Fireplace", "Garden", "Breakfast"]
            }
        ]

        places = []
        for p_data in places_data:
            owner = User.query.filter_by(email=p_data["owner_email"]).first()
            if not owner:
                print(f"Owner {p_data['owner_email']} not found, skipping place {p_data['title']}")
                continue

            place = Place.query.filter_by(title=p_data["title"]).first()
            if not place:
                place = Place(
                    title=p_data["title"],
                    description=p_data["description"],
                    price=p_data["price"],
                    latitude=p_data["latitude"],
                    longitude=p_data["longitude"],
                    owner_id=owner.id,
                    rooms=p_data["rooms"],
                    capacity=p_data["capacity"],
                    surface=p_data["surface"]
                )
                db.session.add(place)
                db.session.flush()  # Pour récupérer place.id avant commit
                for amenity_name in p_data["amenities"]:
                    amenity = Amenity.query.filter_by(name=amenity_name).first()
                    if amenity:
                        place.add_amenity(amenity)
            places.append(place)
        db.session.commit()
        print(f"Created {len(places)} places")

        # Reviews
        print("Creating reviews...")
        reviews_data = [
            {
                "text": "We had a wonderful time in this apartment. The location is perfect and everything was clean and comfortable.",
                "rating": 5,
                "place_title": "Cozy Apartment in Paris",
                "user_email": "jane.smith@example.com"
            },
            {
                "text": "The apartment was nice and well-located. Some minor issues but overall a good experience.",
                "rating": 4,
                "place_title": "Cozy Apartment in Paris",
                "user_email": "marie.dupont@example.com"
            }
        ]

        for r_data in reviews_data:
            place = Place.query.filter_by(title=r_data["place_title"]).first()
            user = User.query.filter_by(email=r_data["user_email"]).first()
            if not place or not user:
                print(f"Skipping review for place '{r_data.get('place_title')}' by '{r_data.get('user_email')}' due to missing user or place")
                continue

            # Check existing review by the same user for the same place
            review = Review.query.filter_by(user_id=user.id, place_id=place.id).first()
            if not review:
                review = Review(
                    text=r_data["text"],
                    rating=r_data["rating"],
                    place_id=place.id,
                    user_id=user.id
                )
                db.session.add(review)
        db.session.commit()
        print(f"Created {len(reviews_data)} reviews")

        # Summary
        print("\nDatabase populated successfully!")
        print(f"Summary:")
        print(f"  - Users: {User.query.count()}")
        print(f"  - Places: {Place.query.count()}")
        print(f"  - Amenities: {Amenity.query.count()}")
        print(f"  - Reviews: {Review.query.count()}")


if __name__ == "__main__":
    populate_database()
