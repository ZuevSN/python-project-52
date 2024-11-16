from django.test import TestCase
from django.urls import reverse_lazy
import json
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from task_manager.users.models import CustomUser
from task_manager.tasks.models import Task


class TasksTestCase(TestCase):
    fixtures = ['users.json', 'statuses.json', 'labels.json', 'tasks.json']

    def setUp(self):
        self.client.force_login(CustomUser.objects.get(pk=1))
        with open(settings.DATA_FOR_TEST, 'r') as file:
            self.test_data = json.load(file)
        self.task_data = self.test_data['task']
        self.updated_task_data = self.test_data['updated_task']

    def test_create_task(self):
        response = self.client.get(reverse_lazy('create_task'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _('Create task'))

        response = self.client.post(
            reverse_lazy('create_task'),
            data=self.task_data,
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _('The task was created successfully')
        )

        last_task = Task.objects.last()
        self.assertEqual(str(last_task), 'Do project-52')

    def test_update_task(self):
        response = self.client.post(
            reverse_lazy('update_task', kwargs={'pk': 1}),
            data=self.updated_task_data,
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _('The task has been successfully changed')
        )
        self.assertEqual(Task.objects.get(pk=1).name, 'Do all projects')
        self.assertEqual(Task.objects.get(pk=1).status.name, 'in work')
        self.assertEqual(Task.objects.get(pk=1).executor.username, 'PetrovP')

    def test_delete_task(self):
        response = self.client.get(
            reverse_lazy('delete_task', kwargs={'pk': 2}),
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _('Only the author of the task can delete it.')
        )

        response = self.client.get(
            reverse_lazy('delete_task', kwargs={'pk': 1}),
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _("Yes, delete")
        )

        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': 1}),
            follow=True
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            _('The task was successfully deleted')
        )
        self.assertFalse(Task.objects.filter(name='DO Tests for project').exists())

    def test_filter_task(self):
        response = self.client.get(
            reverse_lazy('tasks'),
            {'status': '1', 'executor': 1, 'labels': 1, 'user_tasks': 'on'}
        )

        self.assertContains(response, 'DO Tests for project')
        self.assertNotContains(response, 'fix project')
    
    def test_task_list(self):
        response = self.client.get(reverse_lazy('tasks'))

        self.assertContains(response, 'DO Tests for project')
        self.assertContains(response, 'fix project')