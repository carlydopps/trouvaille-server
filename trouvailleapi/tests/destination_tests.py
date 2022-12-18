import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from trouvailleapi.models import Traveler, Destination


class DestinationTests(APITestCase):

    fixtures = ['users', 'tokens', 'travelers', 'destinations']

    def setUp(self):
        self.traveler = Traveler.objects.first()
        token = Token.objects.get(user=self.traveler.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_destination(self):
        """
        Ensure we can get an existing destination.
        """

        destination = Destination()
        destination.city = 'Leavenworth'
        destination.state = 'Washington'
        destination.country = 'US'
        destination.save()

        response = self.client.get(f"/destinations/{destination.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['city'], 'Leavenworth')
        self.assertEqual(json_response['state'], 'Washington')
        self.assertEqual(json_response['country'], 'US')

    def test_create_destination(self):
        """
        Ensure we can create a new destination.
        """
        
        url = "/destinations"
        data = {
            'city': 'St. George',
            'state': 'Utah',
            'country': 'US'
        }
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['city'], 'St. George')
        self.assertEqual(json_response['state'], 'Utah')
        self.assertEqual(json_response['country'], 'US')

    def test_change_destination(self):
        """
        Ensure we can change an existing destination.
        """
        destination = Destination()
        destination.city = 'Denver'
        destination.state = 'Colorado'
        destination.country = 'US'
        destination.save()

        data = {
            'city': 'Boulder',
            'state': 'Colorado',
            'country': 'US'
        }

        response = self.client.put(f"/destinations/{destination.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/destinations/{destination.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['city'], 'Boulder')
        self.assertEqual(json_response['state'], 'Colorado')
        self.assertEqual(json_response['country'], 'US')

    def test_delete_destination(self):
        """
        Ensure we can delete an existing destination.
        """
        destination = Destination()
        destination.city = 'Dillon'
        destination.state = 'Colorado'
        destination.country = 'US'
        destination.save()

        response = self.client.delete(f"/destinations/{destination.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/destinations/{destination.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)