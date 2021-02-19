from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from django import urls
from django.contrib.auth import get_user_model
import pytest

# Create your tests here.
# class TestSetUp(APITestCase):

#     def setUp(self):
#         self.register_url = reverse('register')
#         self.login_url = reverse('login')

#         user_data = {
#             'email':"adminme@gmail.com",
#             'username':"adminme",
#             'password':"123456",
#         }

#         return super().setUp()

#     def tearDown(self):
#         return super().tearDown()

@pytest.mark.parametrize('param', [
    ('login'),
    ('register'),
])

def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200
