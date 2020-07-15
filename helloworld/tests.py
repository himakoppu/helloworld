from django.test import TestCase


class LandingViewTests(TestCase):
    """ Tests for LandingView. """

    def test_landing_view_get(self):
        """ Test GET request to / without Accept in headers. """

        response = self.client.get(path='')
        self.assertEqual(response.status_code, 200)
        assert response.has_header("Content-Type")
        self.assertEqual(response["Content-Type"], "text/html")
        self.assertEqual(response.content, b"<p>Hello, World</p>")
        self.assertEqual(response.content.decode("utf-8"), "<p>Hello, World</p>")

    def test_landing_view_get_as_json(self):
        """ Test GET request to / with Accept as 'application/json' in headers. """

        response = self.client.get(path='', HTTP_ACCEPT="application/json")
        self.assertEqual(response.status_code, 200)
        assert response.has_header("Content-Type")
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(response.content, b'{"message": "Hello, World"}')
        assert response.json()["message"] == "Hello, World"

    def test_landing_view_empty_post(self):
        """ Test POST request to / with empty data. """

        response = self.client.post(path='', data='', content_type="application/json")
        self.assertEqual(response.status_code, 400)
        assert response.json()["error"] == "Data cannot be empty"

    def test_landing_view_invalid_post(self):
        """ Test POST request to / invalid data. """

        response = self.client.post(path='', data="name", content_type="application/json")
        self.assertEqual(response.status_code, 400)
        assert "Expecting value: line 1 column 1" in response.json()["error"]

    def test_landing_view_valid_post(self):
        """ Test POST request to / valid data. """

        response = self.client.post(path='', data={"name": "test"}, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode("utf-8"), "Post successful!")
