from django.core.management.base import BaseCommand
from authapp.models import CustomUser

from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Создает случайного суперпользователя'

    def handle(self, *args, **kwargs):
        name = get_random_string(7)
        CustomUser.objects.create_superuser(username=name, email=f'{name}@defult.ru', password='1234567890')
