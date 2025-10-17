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
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test",
            "last_name": "test",
            "email": "test@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test")
        self.assertEqual(response.json["last_name"], "test")
        self.assertEqual(response.json["email"], "test@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])

    def test_create_place_invalid_title(self):
        """
        Test creating a new place with invalid title.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test1",
            "last_name": "test1",
            "email": "test1@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test1")
        self.assertEqual(response.json["last_name"], "test1")
        self.assertEqual(response.json["email"], "test1@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_description(self):
        """
        Test creating a new place with invalid description.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test2",
            "last_name": "test2",
            "email": "test2@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test2")
        self.assertEqual(response.json["last_name"], "test2")
        self.assertEqual(response.json["email"], "test2@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "",
            "description": "dzazadazdjhazidujzd azdzajazjoidazzdaojdazjdazdjzadzadazd azdadazd azdza zad azdza azzadza zaza  zaddazdazd azdazdazdjoazduazyhdazuihd zahda zidazjazudhauidhazhzdhzaui dhazhuazh iduhaziuhazuiuiazhduiazdhh iuhaid haziudhaiuzh jzajdajziodioazjazidjaziodz ajiodjaijziaojd oiazjzjd aoijdioazjiaz dijdzja oijdiozjd jajdoiazjda",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_price(self):
        """
        Test creating a new place with invalid price.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test3",
            "last_name": "test3",
            "email": "test3@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test3")
        self.assertEqual(response.json["last_name"], "test3")
        self.assertEqual(response.json["email"], "test3@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "abcd",
            "description": "",
            "price": -200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_latitude(self):
        """
        Test creating a new place with invalid latitude.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test4",
            "last_name": "test4",
            "email": "test4@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test4")
        self.assertEqual(response.json["last_name"], "test4")
        self.assertEqual(response.json["email"], "test4@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "abcd",
            "description": "",
            "price": 3200,
            "latitude": -200,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/api/v1/places/', json={
            "title": "abcd",
            "description": "",
            "price": 3200,
            "latitude": 200,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_longitude(self):
        """
        Test creating a new place with invalid longitude.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test5",
            "last_name": "test5",
            "email": "test5@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test5")
        self.assertEqual(response.json["last_name"], "test5")
        self.assertEqual(response.json["email"], "test5@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "abcd",
            "description": "",
            "price": 3200,
            "latitude": 20,
            "longitude": 340,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)

        response = self.client.post('/api/v1/places/', json={
            "title": "abcd",
            "description": "",
            "price": 3200,
            "latitude": 20,
            "longitude": -340,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 400)

    def test_create_place_invalid_owner_id(self):
        """
        Test creating a new place with invalid owner_id.
        """
        response = self.client.post('/api/v1/places/', json={
            "title": "abcd",
            "description": "",
            "price": 3200,
            "latitude": 20,
            "longitude": 340,
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
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test6",
            "last_name": "test6",
            "email": "test6@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test6")
        self.assertEqual(response.json["last_name"], "test6")
        self.assertEqual(response.json["email"], "test6@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "some random Appartement",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id,
            "amenities": [],
            "rooms": 2,
            "capacity": 3,
            "surface": 2
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "some random Appartement")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertEqual(response.json["rooms"], 2)
        self.assertEqual(response.json["capacity"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertTrue(response.json["owner_id"])

        placeid = response.json["id"]
        response = self.client.get('/api/v1/places/' + placeid)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "some random Appartement")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])
        self.assertTrue(response.json["amenities"])
        self.assertEqual(response.json["rooms"], 2)
        self.assertEqual(response.json["capacity"], 3)
        self.assertEqual(response.json["surface"], 2)
        self.assertTrue(response.json["owner_id"])

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
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test7",
            "last_name": "test7",
            "email": "test7@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test7")
        self.assertEqual(response.json["last_name"], "test7")
        self.assertEqual(response.json["email"], "test7@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "some random Appartement",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "some random Appartement")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])

        placeid = response.json["id"]
        response = self.client.post('/api/v1/places/' + placeid, json={
            "title": "updated Appartement",
            "description": "some updated Appartement",
            "price": 3200,
            "latitude": 34,
            "longitude": 25,
            "owner_id": owner_id
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Place updated successfully")

    def test_updating_place_invalid_title(self):
        """
        Test updating a place with invalid title.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test8",
            "last_name": "test8",
            "email": "test8@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test8")
        self.assertEqual(response.json["last_name"], "test8")
        self.assertEqual(response.json["email"], "test8@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "some random Appartement",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "some random Appartement")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])

        placeid = response.json["id"]
        response = self.client.put('/api/v1/places/' + placeid, json={
            "title": "",
            "description": "some updated Appartement",
            "price": 3200,
        })

        self.assertEqual(response.status_code, 400)

    def test_updating_place_invalid_description(self):
        """
        Test updating a place with invalid description.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test9",
            "last_name": "test9",
            "email": "test9@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test9")
        self.assertEqual(response.json["last_name"], "test9")
        self.assertEqual(response.json["email"], "test9@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "some random Appartement",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "some random Appartement")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])

        placeid = response.json["id"]
        response = self.client.put('/api/v1/places/' + placeid, json={
            "title": "Appartement",
            "description": "zadazdazd azadz zadazdazdaz dazazd azdazaz adz dazd aazdazdzad azdza azdazd ad adazd azdazd azd azda zdazazdazdaz dazdaz azdaz dazdazndaz diaznduazhdhzaiud ahzuidhazd uazhdu hazuidh azhdui azhd au",
            "price": 3200,
        })

        self.assertEqual(response.status_code, 400)

    def test_updating_place_invalid_price(self):
        """
        Test updating a place with invalid price.
        """
        response = self.client.post('/api/v1/users/', json={
            "first_name": "test10",
            "last_name": "test10",
            "email": "test10@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json["first_name"], "test10")
        self.assertEqual(response.json["last_name"], "test10")
        self.assertEqual(response.json["email"], "test10@example.com")

        owner_id = response.json["id"]
        response = self.client.post('/api/v1/places/', json={
            "title": "Appartement",
            "description": "some random Appartement",
            "price": 3200,
            "latitude": 12,
            "longitude": 34,
            "owner_id": owner_id
        })
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json["id"])
        self.assertEqual(response.json["title"], "Appartement")
        self.assertEqual(response.json["description"], "some random Appartement")
        self.assertEqual(response.json["latitude"], 12)
        self.assertEqual(response.json["longitude"], 34)
        self.assertTrue(response.json["owner_id"])

        placeid = response.json["id"]
        response = self.client.put('/api/v1/places/' + placeid, json={
            "title": "Appartement",
            "description": "zadazdazd azadz zadazdazdaz dazazd azdazaz adz dazd aazdazdzad azdza azdazd ad adazd azdazd azd azda zdazazdazdaz dazdaz azdaz dazdazndaz diaznduazhdhzaiud ahzuidhazd uazhdu hazuidh azhdui azhd au",
            "price": -3200,
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
