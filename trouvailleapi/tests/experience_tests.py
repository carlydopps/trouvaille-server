import json
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from trouvailleapi.models import Traveler, Experience


class ExperienceTests(APITestCase):

    fixtures = ['users', 'tokens', 'travelers', 'experiences', 'experience_types']

    def setUp(self):
        self.traveler = Traveler.objects.first()
        token = Token.objects.get(user=self.traveler.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_get_experience(self):
        """
        Ensure we can get an existing experience.
        """

        experience = Experience()
        experience.title = 'Sand boarding'
        experience.address = '4981 Oregon Coast Hwy, Florence, OR 97439'
        experience.website_url = 'https://sandmasterpark.com/'
        experience.experience_type_id = 1
        experience.save()

        response = self.client.get(f"/experiences/{experience.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['title'], 'Sand boarding')
        self.assertEqual(json_response['address'], '4981 Oregon Coast Hwy, Florence, OR 97439')
        self.assertEqual(json_response['website_url'], 'https://sandmasterpark.com/')
        self.assertEqual(json_response['experience_type']['id'], 1)

    def test_create_experience(self):
        """
        Ensure we can create a new experience.
        """
        
        url = "/experiences"
        data = {
            'title': 'Snowboarding at Eldora Mountain',
            'address': '2861 Eldora Ski Rd, Nederland, CO 80466',
            'websiteUrl': 'https://www.eldora.com/?utm_source=google&utm_medium=gmb&utm_campaign=profile',
            'experienceTypeId': 1
        }
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response['title'], 'Snowboarding at Eldora Mountain')
        self.assertEqual(json_response['address'], '2861 Eldora Ski Rd, Nederland, CO 80466')
        self.assertEqual(json_response['website_url'], 'https://www.eldora.com/?utm_source=google&utm_medium=gmb&utm_campaign=profile')
        self.assertEqual(json_response['experience_type']['id'], 1)

    def test_change_experience(self):
        """
        Ensure we can change an existing experience.
        """
        experience = Experience()
        experience.title = 'Skiing at A-Basin'
        experience.address = '28194 US-6, Dillon, CO 80435'
        experience.website_url = 'https://www.arapahoebasin.com/'
        experience.experience_type_id = 1
        experience.save()

        data = {
            'title': 'Skiing at Arapahoe Basin',
            'address': '28194 US-6, Dillon, CO 80435',
            'websiteUrl': 'https://www.arapahoebasin.com/about-arapahoe-basin/',
            'experienceTypeId': 2
        }

        response = self.client.put(f"/experiences/{experience.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/experiences/{experience.id}")
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response['title'], 'Skiing at Arapahoe Basin')
        self.assertEqual(json_response['address'], '28194 US-6, Dillon, CO 80435')
        self.assertEqual(json_response['website_url'], 'https://www.arapahoebasin.com/about-arapahoe-basin/')
        self.assertEqual(json_response['experience_type']['id'], 2)

    def test_delete_experience(self):
        """
        Ensure we can delete an existing experience.
        """
        experience = Experience()
        experience.title = 'Skiing at A-Basin 2.0'
        experience.address = '28194 US-6, Dillon, CO 80435'
        experience.website_url = 'https://www.arapahoebasin.com/'
        experience.experience_type_id = 1
        experience.save()

        response = self.client.delete(f"/experiences/{experience.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(f"/experiences/{experience.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)