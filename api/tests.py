from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase


# class UserApiTestCase(APITestCase):
#
#     def test_get(self):
#         url = reverse('users-list')
#         response = self.client.get(url)
from profile.models import Profile


class ArticleTestCase(TestCase):

    def setUp(self) -> None:
        self.profile = Profile.objects.create(
            description="Test title",

        )
        self.client = Client()

    def test_create_profile(self):
        self.assertEqual(Profile.objects.count(), 1)

    def test_profile_str(self):
        self.assertEqual(str(self.profile),
                         "Test title")

    # def test_api_get_profile(self):
    #     response_json = self.client.get('/api/articles/').json()
    #
    #     self.assertEqual(response_json['count'], 1)
    #     self.assertEqual(
    #         response_json['count'][0],
    #         {
    #             "title": "Test title",
    #             "id": 1,
    #             "content": "test content",
    #             "author": None,
    #             "link": 'http://testserver/api/articles/1/'
    #         },
    #     )
