import unittest
from app import create_app


class TestPlaceEndpoints(unittest.TestCase):
    """
    Class for testing place-related API endpoints.
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
    def test_create_place(self):
        """
        Test creating a new place with valid data.
        """
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": "jhon"
        })
        self.assertEqual(response.status_code, 201)

    def test_create_place_invalid_title(self):
        """
        Test creating a new place with invalid title.
        """
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_description(self):
        """
        Test creating a new place with invalid description.
        """
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_price(self):
        """
        Test creating a new place with invalid price.
        """
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_latitude(self):
        """
        Test creating a new place with invalid latitude.
        """
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_longitude(self):
        """
        Test creating a new place with invalid longitude.
        """
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_owner_id(self):
        """
        Test creating a new place with invalid owner_id.
        """
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    """
    --GET--
    """
    def test_fetch_place_fetchall(self):
        """
        Test fetch place fetching all.
        """
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)

    def test_fetch_place_id(self):
        """
        Test fetch place fetching with id.
        """
        placeid = ""
        response = self.client.get('/api/v1/places/' + placeid)
        self.assertEqual(response.status_code, 200)

    def test_fetch_place_invalid_id(self):
        """
        Test fetch place fetching all.
        """
        placeid = "invalid_id"
        response = self.client.get('/api/v1/places/' + placeid)
        self.assertEqual(response.status_code, 404)

    """
    --PUT--
    """
    def test_updating_place(self):
        """
        Test updating a place with valid data.
        """
        placeid = ""
        response = self.client.post('/api/v1/places/' + placeid, json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": "jhon"
        })
        self.assertEqual(response.status_code, 201)

    def test_updating_place_invalid_title(self):
        """
        Test updating a place with invalid title.
        """
        placeid = ""
        response = self.client.post('/api/v1/places/' + placeid, json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_updating_place_invalid_description(self):
        """
        Tes updating a place with invalid description.
        """
        placeid = ""
        response = self.client.post('/api/v1/places/' + placeid, json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_updating_place_invalid_price(self):
        """
        Test updating a place with invalid price.
        """
        placeid = ""
        response = self.client.post('/api/v1/places/' + placeid, json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_updating_place_invalid_latitude(self):
        """
        Test updating a place with invalid latitude.
        """
        placeid = ""
        response = self.client.post('/api/v1/places/' + placeid, json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_updating_place_invalid_longitude(self):
        """
        Test updating a place with invalid longitude.
        """
        placeid = ""
        response = self.client.post('/api/v1/places/' + placeid, json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_updating_place_invalid_owner_id(self):
        """
        Test creating a new place with invalid owner_id.
        """
        placeid = ""
        response = self.client.post('/api/v1/places/' + placeid, json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_updating_place_invalid_id(self):
        """
        Test creating a new place with invalid owner_id.
        """
        placeid = "invalid_id"
        response = self.client.post('/api/v1/places/' + placeid, json={
            "title": "",
            "description": "",
            "price": -12,
            "latitude": -200,
            "longitude": 200,
            "owner_id": ""
        })
        self.assertEqual(response.status_code, 404)
