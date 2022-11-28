from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import regsitration_view
urlpatterns=[
    path('login/',obtain_auth_token,name='login'),
    path('register/',regsitration_view,name='register'),
]