import unittest
from app import create_app


class TestUserEndpoints(unittest.TestCase):
    """
    Class for testing user-related API endpoints.
    """
    def setUp(self):
        """
        initialize the test client and app context.
        """
        self.app = create_app()
        self.client = self.app.test_client()

    """
    --POST--
    """
    def test_create_user(self):
        """
        Test creating a new user with valid data.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_first_name(self):
        """
        Test creating a new user with invalid first name.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_last_name(self):
        """
        Test creating a new user with invalid last name.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "jhon",
            "last_name": "",
            "email": "john.doe@example.com"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_email(self):
        """
        Test creating a new user with invalid email.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "jhon",
            "last_name": "Doe",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_duplicate_email(self):
        """
        Test creating a new user with duplicate email.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "jhon",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 400)

    """
    --GET--
    """
    def test_fetching_users_fetchall(self):
        """
        Test fetching all users.
        """
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)

    def test_fetching_users_fetchid(self):
        """
        Test fetching user id.
        """
        userid = ""
        response = self.client.get('/api/v1/users/' + userid)
        self.assertEqual(response.status_code, 200)

    """
    --PUT--
    """
    def test_updating_user(self):
        """
        Test updating a user.
        """
        userid = ""
        response = self.client.put('/api/v1/users/' + userid, json={
            "first_name": "jhon",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 200)

    def test_updating_nonexistent_user(self):
        """
        Test updating a nonexistent user.
        """
        response = self.client.put('/api/v1/users/"user id"', json={
            "first_name": "jhon",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 404)

    def test_updating_user_invalid_first_name(self):
        """
        Test updating with invalid first_name.
        """
        userid = ""
        response = self.client.put('/api/v1/users/' + userid, json={
            "first_name": "",
            "last_name": "Doe",
            "email": "jhon.doe@example.com"
        })
        self.assertEqual(response.status_code, 400)

    def test_updating_user_invalid_last_name(self):
        """
        Test updating with invalid last_name.
        """
        userid = ""
        response = self.client.put('/api/v1/users/' + userid, json={
            "first_name": "jhon",
            "last_name": "",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(response.status_code, 400)

    def test_updating_user_invalid_email(self):
        """
        Test updating with invalid email.
        """
        userid = ""
        response = self.client.put('/api/v1/users/' + userid, json={
            "first_name": "jhon",
            "last_name": "Doe",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)
