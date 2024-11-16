from task_manager.users.models import CustomUser
from django.test import TestCase
from django.urls import reverse_lazy
import json
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class UsersTestCase(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']

    def setUp(self):
        with open(settings.DATA_FOR_TEST, 'r') as file:
            self.test_data = json.load(file)
        self.user_data = self.test_data['user']
        self.updated_user_data = self.test_data['updated_user']

    def test_user_list(self):
        response = self.client.get(reverse_lazy('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_list.html')
        self.assertContains(response, 'Ivan Ivanov')
        self.assertContains(response, 'Petr Petrov')
        self.assertEqual(len(response.context['users']), 2)

    def test_create_user(self):
        response = self.client.get(reverse_lazy('create_user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')
        user_data = self.user_data
        response = self.client.post(
            reverse_lazy('create_user'),
            data=user_data,
            follow=True
        )

        self.assertRedirects(response, reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('The user was created successfully'))
        last_user = CustomUser.objects.last()
        self.assertEqual(str(last_user), 'Sidor Sidorov')
        self.assertEqual(last_user.username, 'SidorovS')

    def test_update_user(self):
        response = self.client.get(
            reverse_lazy('update_user', kwargs={'pk': 1}),
            follow=True
        )
        self.assertRedirects(response, reverse_lazy('login'))
        self.assertContains(
            response,
            _('You are not logged in! Please log in.')
        )
        self.user = CustomUser.objects.create_user(
            username=self.user_data.get('username'),
            password=self.user_data.get('password1')
        )
        self.client.force_login(self.user)
        response = self.client.get(
            reverse_lazy('update_user', kwargs={'pk': 1}),
            follow=True
        )
        self.assertRedirects(response, reverse_lazy('users'))
        self.assertContains(
            response,
            _('You dont have permissions to modify another user.')
        )
        response = self.client.get(
            reverse_lazy('update_user', kwargs={'pk': 3}),
            follow=True
        )
        self.assertTemplateUsed(response, 'form.html')
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse_lazy('update_user', kwargs={'pk': 3}),
            data=self.updated_user_data,
            follow=True
        )
        self.assertRedirects(response, reverse_lazy('users'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('The user has been successfully changed'))
        self.assertEqual(CustomUser.objects.get(pk=3).username, 'NesidorovS')

    def test_delete_user(self):
        response = self.client.get(
            reverse_lazy('delete_user', kwargs={'pk': 1}),
            follow=True
        )

        self.assertRedirects(response, reverse_lazy('login'))
        self.assertContains(
            response,
            _('You are not logged in! Please log in.')
        )

        self.user = CustomUser.objects.create_user(
            username=self.user_data.get('username'),
            password=self.user_data.get('password1')
        )
        self.client.force_login(self.user)
        response = self.client.get(
            reverse_lazy('delete_user', kwargs={'pk': 1}),
            follow=True
        )
        self.assertRedirects(response, reverse_lazy('users'))
        self.assertContains(
            response,
            _('You dont have permissions to modify another user.')
        )

        response = self.client.get(
            reverse_lazy('delete_user', kwargs={'pk': 3}),
            follow=True
        )
        self.assertTemplateUsed(response, 'delete_form.html')
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': 3}),
            follow=True
        )

        self.assertRedirects(response, reverse_lazy('users'))
        self.assertContains(response, _('The user was successfully deleted'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['users']), 2)

        self.client.force_login(CustomUser.objects.get(pk=1))
        response = self.client.get(
            reverse_lazy('delete_user', kwargs={'pk': 1}),
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _('Yes, delete')
        )

        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': 1}),
            follow=True
        )

        self.assertRedirects(response, reverse_lazy('users'))
        self.assertContains(
            response,
            _('It is not possible to delete a user because it is being used')
        )
