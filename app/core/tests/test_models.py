from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        name = 'Test User'
        password = 'Testpass123'

        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email for a new user is normalized"""
        email = 'test@EXAMPLE.COM'
        user = get_user_model().objects.create_user(
            email=email,
            name='Test User',
            password='test123'
        )
        self.assertEqual(user.email, email.lower())
    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a ValueError."""
        
        with self.assertRaises(ValueError) as context:
            get_user_model().objects.create_user(None, 'test123')
            
        self.assertEqual(str(context.exception), 'Users must have an email address')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
        