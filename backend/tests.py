from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from . import views


# Create your tests here.
class TestOrder(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.OrderViewSet.as_view({'get': 'list'})
        self.uri = '/orders/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code,
            200,
            "looking 200 status response,but the status is {}.".format(response.status_code)
        )
