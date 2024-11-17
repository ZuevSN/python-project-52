from django.test import TestCase
from django.urls import reverse_lazy
import json
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from task_manager.users.models import CustomUser
from task_manager.labels.models import Label


class LabelsTestCase(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']

    def setUp(self):
        with open(settings.DATA_FOR_TEST, 'r') as file:
            self.test_data = json.load(file)
        self.label_data = self.test_data['label']
        self.updated_label_data = self.test_data['updated_label']

    def test_label_list(self):
        self.client.force_login(CustomUser.objects.get(pk=1))
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/label_list.html')
        self.assertContains(response, 'django')
        self.assertContains(response, 'flask')
        self.assertContains(response, 'FastApi')
        self.assertEqual(len(response.context['labels']), 3)

    def test_create_label(self):
        response = self.client.get(reverse_lazy('create_label'), follow=True)

        self.assertRedirects(response, reverse_lazy('login'))
        self.assertContains(
            response,
            _('You are not logged in! Please log in.')
        )

        self.client.force_login(CustomUser.objects.get(pk=1))
        response = self.client.get(reverse_lazy('create_label'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

        response = self.client.post(
            reverse_lazy('create_label'),
            data=self.label_data,
            follow=True
        )

        self.assertRedirects(response, reverse_lazy('labels'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('The label was created successfully'))

        last_label = Label.objects.last()

        self.assertEqual(str(last_label), 'cherrypy')

    def test_update_label(self):
        self.client.force_login(CustomUser.objects.get(pk=1))
        response = self.client.post(
            reverse_lazy('update_label', kwargs={'pk': 1}),
            data=self.updated_label_data,
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _('The label has been successfully changed')
        )
        self.assertEqual(Label.objects.get(pk=1).name, 'pandas')

    def test_delete_label(self):
        self.client.force_login(CustomUser.objects.get(pk=1))
        response = self.client.get(
            reverse_lazy('delete_label', kwargs={'pk': 3}),
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _('Yes, delete')
        )

        response = self.client.post(
            reverse_lazy('delete_label', kwargs={'pk': 3}),
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _('The label was successfully deleted')
        )
        self.assertFalse(Label.objects.filter(name='FastApi').exists())

        response = self.client.get(
            reverse_lazy('delete_label', kwargs={'pk': 1}),
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _('Yes, delete')
        )

        response = self.client.post(
            reverse_lazy('delete_label', kwargs={'pk': 1}),
            follow=True
        )

        self.assertRedirects(response, reverse_lazy('labels'))
        self.assertContains(
            response,
            _('It is not possible to delete the label because it is being used')
        )
