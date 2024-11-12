from task_manager.users.models import CustomUser
from django.test import TestCase
from django.urls import reverse
from django.core.management import call_command

class UsersTestCase(TestCase):
    def setUp(self):
        fixtures = ['users.json']
        for fixture in fixtures:
            call_command('loaddata', fixture)

    def test_user_list(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'users/user_list.html')
        self.assertContains(response, 'Ivan Ivanov')
        self.assertContains(response, 'Petr Petrov')
        self.assertContains(response, 'Sidor Sidorov')
        self.assertEqual(len(response.context['users']),3)
