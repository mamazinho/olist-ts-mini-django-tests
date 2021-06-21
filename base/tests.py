from django.test import TestCase


class TestBase(TestCase):
    def setUp(self):
        self.register_account_to_log = {
            "email": "login@gmail.com",
            "password": "loginpasswd",
            "username": "login",
        }

    def test_route_status_200(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_route_products_returning_an_valid_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'base.html')
