import unittest
from app import create_app


class TestReviewEndpoints(unittest.TestCase):
    """
    Class for testing Amenity-related API endpoints.
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
    def test_create_Amenity(self):
        """
        Test creating a new user with valid data.
        """
        response = self.client.post('/api/v1/amenities/', json={
            "name": "WI-FI",
        })
        self.assertEqual(response.status_code, 201)

    def test_create_Amenity_invalid_data(self):
        """
        Test creating a new user with invalid data.
        """
        response = self.client.post('/api/v1/amenities', json={
            "name": "",
        })
        self.assertEqual(response.status_code, 400)

    """
    --GET--
    """
    def test_fetch_Amenity_fetchall(self):
        """
        Test fetching all amenities.
        """
        response = self.client.get('/api/v1/amenities')
        self.assertEqual(response.status_code, 200)

    def test_fetch_Amenity_fetchid(self):
        """
        Test fetching amenity with id.
        """
        amenityid = ""
        response = self.client.get('/api/v1/amenities/' + amenityid)
        self.assertEqual(response.status_code, 200)

    def test_fetch_Amenity_fetch_invalid_id(self):
        """
        Test fetching invalid amenity.
        """
        amenityid = ""
        response = self.client.get('/api/v1/amenities/' + amenityid)
        self.assertEqual(response.status_code, 404)

    """
    --PUT--
    """
    def test_update_Amenity(self):
        """
        Test updating amenity.
        """
        amenityid = ""
        response = self.client.get('/api/v1/amenities/' + amenityid)
        self.assertEqual(response.status_code, 200)

    def test_update_Amenity_invalid_id(self):
        """
        Test updating invalid id.
        """
        amenityid = ""
        response = self.client.get('/api/v1/amenities/' + amenityid)
        self.assertEqual(response.status_code, 404)

    def test_update_Amenity_invalid_text(self):
        """
        Test updating invalid text.
        """
        amenityid = ""
        response = self.client.get('/api/v1/amenities/' + amenityid)
        self.assertEqual(response.status_code, 400)
