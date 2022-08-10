from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserManagerTests(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(email='user@email.com', password='password')
        self.assertEqual(user.email, 'user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_user()

        with self.assertRaises(TypeError):
            User.objects.create_user(email='')

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo')

    def test_create_superuser(self):
        user = User.objects.create_superuser(email='superuser@email.com', password='password')
        self.assertEqual(user.email, 'superuser@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
