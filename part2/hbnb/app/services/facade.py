from app.persistence.repository import InMemoryRepository
from app.models.user import User


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
        user = User(
            user_data.get("first_name"),
            user_data.get("last_name"),
            user_data.get("email"),
            user_data.get("password")
        )
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

    # Placeholder method for fetching a place by ID
    def get_place(self, place_id):
        # Logic will be implemented in later tasks
        pass
