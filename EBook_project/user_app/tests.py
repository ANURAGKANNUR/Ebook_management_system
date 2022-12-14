from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from  rest_framework import  status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
# Create your tests here.

class RegisterTestCase(APITestCase):
    def test_register(self):
        data={
            'username':"testcase",
            'email':'testcase@gmail.com',
            'password':'Test@123',
            'password2':'Test@123'
        }
        response=self.client.post(reverse('register'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


class LoginTestCase(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="testcase",password="Test@@@123")
        new_token = Token.objects.create(user=self.user)

        self.token = Token.objects.get(user=self.user)

    def test_login(self):
        data={
            'username':"testcase",
            'password':"Test@@@123"
        }
        response=self.client.post(reverse('login'),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

class Test_logout(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="testcase",password="Test@@@123")
        new_token = Token.objects.create(user=self.user)

        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)

    def logout(self):
        response=self.client.get(reverse('logout'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)