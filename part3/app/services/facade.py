from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    """
    Facade class to manage users, places, reviews, and amenities.
    """
    def __init__(self):
        """
        Facade constructor to initialize repositories for
        users, places, reviews, and amenities.
        """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()


    # ----- USER METHODS -----
    """
    --User Methods--
    """
    def create_user(self, user_data):
        """
        Method to create a new user and add it to the user repository.

        Arguments:
            user_data (dict): A dictionary containing user details like
            first_name, last_name, email, and password.

        Returns:
            user (User): The created User object.
        """
        #hashed_password = hash_password(user_data.get("password"))
        user = User(
            user_data.get("first_name"),
            user_data.get("last_name"),
            user_data.get("email"),
            user_data.get("password")
        )
        user.password=user.hash_password(user.password)
        self.user_repo.add(user)
        return user

    def get_all_users(self):
        """
        Get all users from the user repository.
        """
        return self.user_repo.get_all()

    def get_user(self, user_id):
        """
        Get a user by their ID.

        Arguments:
            user_id (str): The ID of the user to retrieve.

        Returns:
            user (User or None): The User object if found, else None.
        """
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """
        Get a user by their email.

        Arguments:
            email (str): The email of the user to retrieve.

        Returns:
            user (User or None): The User object if found, else None.
        """
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, update_data):
        """
        update a user's attributes.

        Arguments:
            user_id (str): The ID of the user to update.
            update_data (dict): A dictionary containing attributes to update.

        Returns:
            user (User): The updated User object.
        """
        self.user_repo.update(user_id, update_data)
    """
    --End of User Methods--
    """

    # ----- AMENITY METHODS -----
    """
    --amenity METHODS--
    """
    def create_amenity(self, amenity_data):
        """
        Create a new amenity and add it to the amenity repository.

        Arguments:
            amenity_data (dict): A dictionary containing
            amenity details like name.

        Returns:
            new_amenity (amenity): The created amenity object.
        """
        new_amenity = Amenity(amenity_data.get("name"))
        self.amenity_repo.add(new_amenity)

        return new_amenity

    def get_amenity(self, amenity_id):
        """
        GET an amenity by its ID.

        Arguments:
            amenity_id (str): The ID of the amenity to retrieve.

        Returns:
            amenity (amenity or None): The amenity object if found, else None.
        """
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        """
        GET all amenities from the amenity repository.

        Returns:
            amenities (list): A list of all amenity objects.
        """
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        """
        Update an amenity's attributes.

        Arguments:
            amenity_id (str): The ID of the amenity to update.
            amenity_data (dict): A dictionary containing attributes to update.
        """
        self.amenity_repo.update(amenity_id, amenity_data)
    """
    --End of amenity METHODS--
    """

    # ----- PLACE METHODS -----
    def create_place(self, place_data):
        if 'rooms' not in place_data:
            raise ValueError("The field 'rooms' is requirement.")
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        self.place_repo.update(place_id, place_data)

    # ----- REVIEW METHODS -----
    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)
        return place.reviews

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        for key, value in review_data.items():
            setattr(review, key, value)
        self.review_repo.update(review_id, review_data)
        return review

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)
