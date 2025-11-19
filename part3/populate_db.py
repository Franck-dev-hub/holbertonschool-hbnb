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

        print("Clearing existing data...")
        db.session.query(Review).delete()
        db.session.query(Place).delete()
        db.session.query(Amenity).delete()
        db.session.query(User).delete()
        db.session.commit()

        # Create users
        print("Creating users...")
        users = [
            User(
                email="john.doe@example.com",
                first_name="John",
                last_name="Doe",
                password="password123",
                is_admin=False
            ),
            User(
                email="jane.smith@example.com",
                first_name="Jane",
                last_name="Smith",
                password="password123",
                is_admin=False
            ),
            User(
                email="admin@hbnb.com",
                first_name="Admin",
                last_name="User",
                password="admin123",
                is_admin=True
            ),
            User(
                email="marie.dupont@example.com",
                first_name="Marie",
                last_name="Dupont",
                password="password123",
                is_admin=False
            ),
            User(
                email="pierre.martin@example.com",
                first_name="Pierre",
                last_name="Martin",
                password="password123",
                is_admin=False
            )
        ]

        for user in users:
            user.save(commit=False)
        db.session.commit()
        print(f"Created {len(users)} users")

        # Create amenities
        print("Creating amenities...")
        amenities_data = [
            "WiFi",
            "Kitchen",
            "Parking",
            "Pool",
            "Air Conditioning",
            "Heating",
            "Washer",
            "Dryer",
            "TV",
            "Gym"
        ]

        amenities = []
        for amenity_name in amenities_data:
            amenity = Amenity(name=amenity_name)
            amenity.save(commit=False)
            amenities.append(amenity)
        db.session.commit()
        print(f"Created {len(amenities)} amenities")

        # Create places
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
                "title": "Charming House in Marseille",
                "description": "Traditional Provençal house with garden, perfect for families. Close to the beach and city center.",
                "price": 150.0,
                "latitude": 43.2965,
                "longitude": 5.3698,
                "rooms": 4,
                "capacity": 1,
                "surface": 20.0,
                "owner_email": "marie.dupont@example.com",
                "amenities": ["WiFi", "Kitchen", "Parking", "Pool", "Washer", "Dryer"]
            },
            {
                "title": "Studio in Nice",
                "description": "Bright and modern studio apartment near the beach. Ideal for a relaxing vacation by the Mediterranean.",
                "price": 75.0,
                "latitude": 43.7102,
                "longitude": 7.2620,
                "rooms": 1,
                "capacity": 10,
                "surface": 200.0,
                "owner_email": "pierre.martin@example.com",
                "amenities": ["WiFi", "Air Conditioning", "TV"]
            },
            {
                "title": "Luxury Villa in Cannes",
                "description": "Stunning villa with private pool and garden. Perfect for a luxurious stay on the French Riviera.",
                "price": 300.0,
                "latitude": 43.5528,
                "longitude": 7.0174,
                "rooms": 5,
                "capacity": 3,
                "surface": 55.0,
                "owner_email": "jane.smith@example.com",
                "amenities": ["WiFi", "Kitchen", "Parking", "Pool", "Air Conditioning", "TV", "Gym", "Washer", "Dryer"]
            },
            {
                "title": "Rustic Cottage in Provence",
                "description": "Authentic Provençal cottage surrounded by lavender fields. Peaceful and romantic setting.",
                "price": 95.0,
                "latitude": 43.8316,
                "longitude": 5.0369,
                "rooms": 2,
                "capacity": 6,
                "surface": 102.0,
                "owner_email": "john.doe@example.com",
                "amenities": ["WiFi", "Kitchen", "Parking", "Heating"]
            }
        ]

        places = []
        for place_data in places_data:
            # Find owner by email
            owner = User.query.filter_by(email=place_data["owner_email"]).first()
            if not owner:
                print(f"Warning: Owner {place_data['owner_email']} not found, skipping place {place_data['title']}")
                continue

            place = Place(
                title=place_data["title"],
                description=place_data["description"],
                price=place_data["price"],
                latitude=place_data["latitude"],
                longitude=place_data["longitude"],
                owner_id=owner.id,
                rooms=place_data["rooms"],
                capacity=place_data["capacity"],
                surface=place_data["surface"]
            )

            # Add amenities to place
            for amenity_name in place_data["amenities"]:
                amenity = Amenity.query.filter_by(name=amenity_name).first()
                if amenity:
                    place.add_amenity(amenity)

            place.save(commit=False)
            places.append(place)

        db.session.commit()
        print(f"Created {len(places)} places")

        # Create reviews
        print("Creating reviews...")
        reviews_data = [
            {
                "title": "Great stay!",
                "text": "We had a wonderful time in this apartment. The location is perfect and everything was clean and comfortable.",
                "rating": 5,
                "place_title": "Cozy Apartment in Paris",
                "user_email": "jane.smith@example.com"
            },
            {
                "title": "Nice place",
                "text": "The apartment was nice and well-located. Some minor issues but overall a good experience.",
                "rating": 4,
                "place_title": "Cozy Apartment in Paris",
                "user_email": "marie.dupont@example.com"
            },
            {
                "title": "Amazing loft!",
                "text": "This loft exceeded our expectations. The views are incredible and the space is very comfortable.",
                "rating": 5,
                "place_title": "Modern Loft in Lyon",
                "user_email": "john.doe@example.com"
            },
            {
                "title": "Perfect for families",
                "text": "We stayed here with our two children and had a fantastic time. The house is spacious and the garden is lovely.",
                "rating": 5,
                "place_title": "Charming House in Marseille",
                "user_email": "pierre.martin@example.com"
            },
            {
                "title": "Beautiful studio",
                "text": "Small but perfectly organized studio. Great location near the beach. Would definitely stay again!",
                "rating": 4,
                "place_title": "Studio in Nice",
                "user_email": "jane.smith@example.com"
            },
            {
                "title": "Luxury experience",
                "text": "Absolutely stunning villa! The pool and garden are beautiful. Worth every penny for a special occasion.",
                "rating": 5,
                "place_title": "Luxury Villa in Cannes",
                "user_email": "john.doe@example.com"
            },
            {
                "title": "Peaceful retreat",
                "text": "A wonderful escape from city life. The cottage is charming and the surroundings are breathtaking.",
                "rating": 5,
                "place_title": "Rustic Cottage in Provence",
                "user_email": "marie.dupont@example.com"
            }
        ]

        reviews = []
        for review_data in reviews_data:
            # Find place by title
            place = Place.query.filter_by(title=review_data["place_title"]).first()
            if not place:
                print(f"Warning: Place {review_data['place_title']} not found, skipping review")
                continue

            # Find user by email
            user = User.query.filter_by(email=review_data["user_email"]).first()
            if not user:
                print(f"Warning: User {review_data['user_email']} not found, skipping review")
                continue

            review = Review(
                title=review_data["title"],
                text=review_data["text"],
                rating=review_data["rating"],
                place_id=place.id,
                place=place,
                user_id=user.id,
                user=user
            )

            review.save(commit=False)
            reviews.append(review)

        db.session.commit()
        print(f"Created {len(reviews)} reviews")

        print("\nDatabase populated successfully!")
        print(f"\nSummary:")
        print(f"  - Users: {User.query.count()}")
        print(f"  - Places: {Place.query.count()}")
        print(f"  - Amenities: {Amenity.query.count()}")
        print(f"  - Reviews: {Review.query.count()}")


if __name__ == "__main__":
    populate_database()
