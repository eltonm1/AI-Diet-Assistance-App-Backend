from django.test import TestCase
from rest_framework.test import APIRequestFactory
# Create your tests here.
from .models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate
from .views import UserViewList

class UserTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
                **{
                    "email" : "test_email@test.com",
                    "date_of_birth" : "2000-01-01",
                    },
        )
        user.set_password("123")
        user.save()
        self.user = user
        self.token = Token.objects.create(user=user)

    def test_get_all_users_authenticated(self):
        factory = APIRequestFactory()
        request = factory.get('/users/')

        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = UserViewList.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_get_all_users_not_authenticated(self):
        factory = APIRequestFactory()
        request = factory.get('/users/')

        response = UserViewList.as_view()(request)
        self.assertEqual(response.status_code, 401)