"""
Tests for models
"""

from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

#def sample_user(email='test@example.com', password='testpass'):
#    """Create a sample user"""
#    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test email is normalized"""
        sample_emails = [
            ['test1@EXAMPLE.com','test1@example.com'],
            ['Test2@Example.com','Test2@example.com'],
            ['TEST3@EXAMPLE.COM','TEST3@example.com'],
            ['test4@example.COM','test4@example.com'],

        ]
        for email,expected in sample_emails :
            user = get_user_model().objects.create_user(email,'sample123')
            self.assertEqual(user.email,expected)

    def test_new_user_without_email_raises_error(self):
        """Test that a user can not register without an email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','test123')

    def test_create_superuser(self):
        """Test create superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)