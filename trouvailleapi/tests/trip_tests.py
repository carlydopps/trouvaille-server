import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from trouvailleapi.models import Trip, Traveler, Experience, Destination


class TripTests(APITestCase):

    fixtures = ['users', 'tokens', 'travelers', 'destinations', 'durations', 'experience_types', 'experiences', 'seasons', 'styles', 'trip_destinations', 'trip_experiences', 'trips']

    def setUp(self):
        self.traveler = Traveler.objects.first()
        token = Token.objects.get(user=self.traveler.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_experience(self):
        """
        Ensure we can get an existing trip.
        """

        trip = Trip()
        trip.title = 'Test Trip to Get'
        trip.summary = 'Summary of test trip'
        trip.traveler_id = 1
        trip.style_id = 1
        trip.season_id = 1
        trip.duration_id = 1
        trip.is_draft = False
        trip.is_upcoming = False
        trip.is_private = False
        trip.modified_date = '2022-08-28T14:51:39.989000Z'
        trip.save()

        exp_1 = Experience.objects.get(pk=1)
        exp_2 = Experience.objects.get(pk=2)
        dest_1 = Destination.objects.get(pk=3)
        dest_2 = Destination.objects.get(pk=4)

        trip.experiences.set([exp_1, exp_2])
        trip.destinations.set([dest_1, dest_2])

        response = self.client.get(f"/trips/{trip.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['title'], 'Test Trip to Get')
        self.assertEqual(json_response['summary'], 'Summary of test trip')
        self.assertEqual(json_response['traveler']['id'], 1)
        self.assertEqual(json_response['style']['id'], 1)
        self.assertEqual(json_response['season']['id'], 1)
        self.assertEqual(json_response['duration']['id'], 1)
        self.assertEqual(json_response['is_draft'], False)
        self.assertEqual(json_response['is_upcoming'], False)
        self.assertEqual(json_response['is_private'], False)
        self.assertEqual(json_response['modified_date'], '2022-08-28T14:51:39.989000Z')
        self.assertEqual(json_response['experiences'][0]['id'], 1)
        self.assertEqual(json_response['experiences'][1]['id'], 2)
        self.assertEqual(json_response['destinations'][0]['id'], 3)
        self.assertEqual(json_response['destinations'][1]['id'], 4)

    def test_create_trip(self):
        """
        Ensure we can create a new trip.
        """
        
        url = "/trips"
        data = {
            'title': 'Test Trip to Post',
            'summary': 'Summary of test trip',
            'styleId': 1,
            'seasonId': 1,
            'durationId': 1,
            'isDraft': False,
            'isUpcoming': False,
            'isPrivate': False
        }

        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['title'], 'Test Trip to Post')
        self.assertEqual(json_response['summary'], 'Summary of test trip')
        self.assertEqual(json_response['traveler']['id'], 1)
        self.assertEqual(json_response['style']['id'], 1)
        self.assertEqual(json_response['season']['id'], 1)
        self.assertEqual(json_response['duration']['id'], 1)
        self.assertEqual(json_response['is_draft'], False)
        self.assertEqual(json_response['is_upcoming'], False)
        self.assertEqual(json_response['is_private'], False)

    def test_change_trip(self):
        """
        Ensure we can change an existing trip.
        """
        trip = Trip()
        trip.title = 'Test Trip to Update'
        trip.summary = 'Summary of test trip'
        trip.traveler_id = 1
        trip.style_id = 1
        trip.season_id = 1
        trip.duration_id = 1
        trip.is_draft = False
        trip.is_upcoming = False
        trip.is_private = False
        trip.modified_date = '2022-08-28T14:51:39.989000Z'
        trip.save()

        exp_1 = Experience.objects.get(pk=1)
        exp_2 = Experience.objects.get(pk=2)
        dest_1 = Destination.objects.get(pk=3)
        dest_2 = Destination.objects.get(pk=4)

        trip.experiences.set([exp_1, exp_2])
        trip.destinations.set([dest_1, dest_2])

        data = {
            'title': 'Edited Test Trip',
            'summary': 'Summary of test trip',
            'styleId': 1,
            'seasonId': 2,
            'durationId': 2,
            'isDraft': False,
            'isUpcoming': True,
            'isPrivate': True
        }

        response = self.client.put(f"/trips/{trip.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/trips/{trip.id}")
        json_response = json.loads(response.content)

        self.assertEqual(json_response['title'], 'Edited Test Trip')
        self.assertEqual(json_response['summary'], 'Summary of test trip')
        self.assertEqual(json_response['traveler']['id'], 1)
        self.assertEqual(json_response['style']['id'], 1)
        self.assertEqual(json_response['season']['id'], 2)
        self.assertEqual(json_response['duration']['id'], 2)
        self.assertEqual(json_response['is_draft'], False)
        self.assertEqual(json_response['is_upcoming'], True)
        self.assertEqual(json_response['is_private'], True)
        self.assertEqual(json_response['experiences'][0]['id'], 1)
        self.assertEqual(json_response['experiences'][1]['id'], 2)
        self.assertEqual(json_response['destinations'][0]['id'], 3)
        self.assertEqual(json_response['destinations'][1]['id'], 4)

    def test_delete_trip(self):
        """
        Ensure we can delete an existing trip.
        """
        trip = Trip()
        trip.title = 'Test Trip to Delete'
        trip.summary = 'Summary of test trip to delete'
        trip.traveler_id = 1
        trip.style_id = 1
        trip.season_id = 1
        trip.duration_id = 1
        trip.is_draft = False
        trip.is_upcoming = False
        trip.is_private = False
        trip.modified_date = '2022-08-28T14:51:39.989000Z'
        trip.save()

        exp_1 = Experience.objects.get(pk=1)
        exp_2 = Experience.objects.get(pk=2)
        dest_1 = Destination.objects.get(pk=3)
        dest_2 = Destination.objects.get(pk=4)

        trip.experiences.set([exp_1, exp_2])
        trip.destinations.set([dest_1, dest_2])

        response = self.client.delete(f"/trips/{trip.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/trips/{trip.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)