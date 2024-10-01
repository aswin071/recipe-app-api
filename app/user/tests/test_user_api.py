from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model


class CreateUserApiTests(TestCase):
    """Test the users API (create)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name'
        }

        url = reverse('create')  # Reverse resolves the name 'create' to the actual URL
        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)  # Check if created successfully
        user = get_user_model().objects.get(**res.data)  # Get the created user by the response data
        self.assertTrue(user.check_password(payload['password']))  # Ensure the password is correct
        self.assertEqual(user.email, payload['email'])  # Ensure the email is correct

    def test_create_user_with_existing_email(self):
        """Test creating user with already existing email fails"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass123',
            'name': 'Test Name'
        }

        get_user_model().objects.create_user(**payload)  # Create a user with the same email
        url = reverse('create')
        res = self.client.post(url, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)  # Check for bad request status

    def test_create_user_invalid_password(self):
        """Test creating user with invalid password fails"""
        payload = {
            'email': 'test@example.com',
            'password': 'pwcjghkcghjk',  # Invalid password (too short)
            'name': 'Test Name'
        }

        url = reverse('create')
        res = self.client.post(url, payload)

        # self.assertEqual(res.status_c)  # Check for bad request status
        self.assertIn('password', res.data)  # Ensure password validation failed
