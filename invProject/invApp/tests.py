from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserAccessTestCase(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='admin', password='admin123', email='admin@example.com')
        self.standard_user = User.objects.create_user(username='user', password='user123')

    def test_admin_access(self):
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('user_management'))
        self.assertEqual(response.status_code, 200)  # Admin should access user management

    def test_standard_user_access(self):
        self.client.login(username='user', password='user123')
        response = self.client.get(reverse('user_management'))
        self.assertEqual(response.status_code, 302)  # Standard user should be redirected