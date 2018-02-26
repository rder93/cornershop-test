from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from todoapp.models import *

# from model_mommy import mommy

# models test
class UserTestCase(TestCase):

    def setUp(self):
        self.user_data = {
            'email': 'ricaldo@gmail.com',
            'username': 'rder93',
            'password': '1512933'
        }
        User.objects.create_user(**self.user_data)

    def test_invalidRegister_user(self):
        # sending a false register data to validate
        response = self.client.post('/api/register/',{'username':'rder93','password':'12345','email': 'ricaldo@gmail.com'})
        self.assertEqual(response.status_code, 400)

    def test_invalidLogin_user(self):
        # sending a false login data to validate
        response = self.client.post('/api/login/',{'username':'rder93','password':'12345','email': 'rder993@gmail.com'})
        self.assertEqual(response.status_code, 400)

    def test_login_user(self):
        # sending login data to validate
        response = self.client.post('/api/login/', self.user_data, follow=True)
        self.assertTrue(response.status_code, 200)


class TodoTestCase(TestCase):

    def setUp(self):
        self.todo_data = {
            'task_name': 'Ir a Argentina',
            'status': False,
        }
        self.todo = Todo.objects.create(**self.todo_data)
        self.subtodo_data = {
            'subtask_name': 'visitar La Plata',
            'status': False,
            'todolist': self.todo
        }
        self.subtodo = SubTodo.objects.create(**self.subtodo_data)

    def test_invalid_todo(self):
        # sending a false todo data, existing task with that name
        response = self.client.post('/api/todo/create/', self.todo_data, follow=True)
        self.assertEqual(response.status_code, 400)

    def test_valid_todo(self):
        # sending a valid todo data to save
        response = self.client.post('/api/todo/create/', {'task_name': 'Crear aplicacion', 'status':False}, follow=True)
        self.assertEqual(response.status_code, 201)

    def test_invalid_subtodo(self):
        # sending a false subtodo data, existing task with that name
        response = self.client.post('/api/subtodo/create/', self.todo_data, follow=True)
        self.assertEqual(response.status_code, 400)

    def test_valid_subtodo(self):
        # sending a valid subtodo data to save
        response = self.client.post('/api/subtodo/create/', {'subtask_name': 'ir a la Patagonia', 'status':False, 'todolist': self.todo.pk}, follow=True)
        self.assertEqual(response.status_code, 201)