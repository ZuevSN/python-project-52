from django.test import TestCase
from django.urls import reverse_lazy
import json
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from task_manager.users.models import CustomUser
from task_manager.statuses.models import Status


class StatusesTestCase(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']

    def setUp(self):
        with open(settings.DATA_FOR_TEST, 'r') as file:
            self.test_data = json.load(file)
        self.status_data = self.test_data['status']
        self.updated_status_data = self.test_data['updated_status']

    def test_status_list(self):
        self.client.force_login(CustomUser.objects.get(pk=1))
        response = self.client.get(reverse_lazy('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/status_list.html')
        self.assertContains(response, 'new')
        self.assertContains(response, 'in work')
        self.assertEqual(len(response.context['statuses']), 2)


    def test_create_status(self):
        response = self.client.get(reverse_lazy('create_status'), follow=True)

        self.assertRedirects(response, reverse_lazy('login'))
        self.assertContains(
            response,
            _('You are not logged in! Please log in.')
        )

        self.client.force_login(CustomUser.objects.get(pk=1))
        response = self.client.get(reverse_lazy('create_status'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

        response = self.client.post(
            reverse_lazy('create_status'),
            data=self.status_data,
            follow=True
        )

        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('The status was created successfully'))

        last_status = Status.objects.last()

        self.assertEqual(str(last_status), 'finished')