from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
# Create your tests here.
from . import models
from .models import Genre, Ebook, Rating
from .serializers import CategorySerializer,EbookSerializer,EbookUpdateSerializer,EbookListSerializer,RatingSerializer

class categoryTest(APITestCase):

    def setUp(self):
        self.user=User.objects.create_user(username="testcase",password="Test@@@123")
        new_token = Token.objects.create(user=self.user)

        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.category=models.Genre.objects.create(category='test1 category')
    def test_category_create(self):

        data={
            'category':'Test_category'
        }
        response=self.client.post(reverse('category-create'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

    def test_category_list(self):
        response=self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_category_ind(self):
        response=self.client.get(reverse('category-detail',args=(self.category.id,)))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    def test_category_update(self):
        data={
            'title':'test3'
        }
        response=self.client.patch(reverse('category-detail',args=(self.category.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_category_delete(self):
        response=self.client.delete(reverse('category-detail',args=(self.category.id,)))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class EbookTest(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="testcase",password="Test@@@123")
        new_token = Token.objects.create(user=self.user)

        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.category=models.Genre.objects.create(category='test1 category')
        self.ebook=models.Ebook.objects.create(title='test',author='test',category=self.category,createdby=self.user)

    def test_create_ebook(self):
        data={
            'title':'Test_title',
            'author':'test_author',
            'category':self.category.id,
            'createdby':self.user
        }
        response=self.client.post(reverse('ebook-create'),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    def test_ebook_list(self):
        response=self.client.get(reverse('ebook-list'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_ebook_update(self):
        data={
            'title':'test1'
        }
        response=self.client.patch(reverse('ebook-update',args=(self.ebook.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_ebook_delete(self):
        response=self.client.delete(reverse('ebook-delete',args=(self.ebook.id,)))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)

class Rating_test(APITestCase):
    def setUp(self):
        self.user=User.objects.create_user(username="testcase",password="Test@@@123")
        new_token = Token.objects.create(user=self.user)

        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.category=models.Genre.objects.create(category='test1 category')
        self.ebook=models.Ebook.objects.create(title='test',author='test',category=self.category,createdby=self.user)
        # self.review=models.Rating.objects.create(review_user=self.user,rating=5,ebook=self.ebook,favourite=True)
    def test_review_create(self):
        data={
            'review_user':self.user,
            'rating':5,
            'ebook':self.ebook,
            'favourite':True
        }
        response=self.client.post(reverse('rating-create',args=(self.ebook.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class Review_update_delete_test(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testcase", password="Test@@@123")
        new_token = Token.objects.create(user=self.user)

        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.category = models.Genre.objects.create(category='test1 category')
        self.ebook = models.Ebook.objects.create(title='test', author='test', category=self.category,
                                                 createdby=self.user)
        self.review=models.Rating.objects.create(review_user=self.user,rating=5,ebook=self.ebook,favourite=True)

    def test_review_view(self):
        reponse=self.client.get(reverse('rating_detail',args=(self.review.id,)))
        self.assertEqual(reponse.status_code,status.HTTP_200_OK)

    def test_review_update(self):
        data={
            'rating':2
        }
        response=self.client.patch(reverse('rating_detail',args=(self.review.id,)),data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_review_delete(self):
        response=self.client.delete(reverse('rating_detail',args=(self.review.id,)))
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)