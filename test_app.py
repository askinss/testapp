import unittest
from app import app


class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        return super().tearDown()

    def test_airports(self):
        response = self.app.get('/airports', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_airports_query(self):
        response = self.app.get('/airports/NL', follow_redirects=True)
        self.assertEqual(response.status_code, 401)
        self.assertTrue(response.content_type == 'application/json')


if __name__ == "__main__":
    unittest.main()
