import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from authapp.views import CustomUserViewSet
from authapp.models import CustomUser
from mainapp.views import ProjectViewSet
from mainapp.models import Project


class TestViewSet(TestCase):
    def test_get_user_list(self):
        factory = APIRequestFactory()
        request = factory.get('/authapp/')
        view = CustomUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/project/', {'project_name': 'Проект тест'}, format='json')
        view = ProjectViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail(self):
        project = mixer.blend(Project)
        client = APIClient()
        response = client.get(f'/project/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user_admin(self):
        user = mixer.blend(CustomUser)
        client = APIClient()
        admin = CustomUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.delete(f'/authapp/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        client.logout()


class TestAPIViewSet(APITestCase):

    def test_get_TODO_list(self):
        response = self.client.get('/TODO/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_TODO_list_admin(self):
        admin = CustomUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.get('/TODO/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()

    def test_edit_user_admin(self):
        user = mixer.blend(CustomUser)
        admin = CustomUser.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'/authapp/{user.id}/', {'username': 'Grin',
                                                            'email': 'L6FZLaI@defult.ru',
                                                            'user_category': 'DV',
                                                            'is_active': True,
                                                            'password': '123456'
                                                            })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = CustomUser.objects.get(id=user.id)
        self.assertEqual(user.username, 'Grin')
        self.client.logout()
