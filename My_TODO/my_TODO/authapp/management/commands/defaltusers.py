from django.core.management.base import BaseCommand
from authapp.models import CustomUser
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = 'Создает случайных пользователей'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Указывает сколько пользователей необходимо создать')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            name = get_random_string(7)
            CustomUser.objects.create_user(username=name, email=f'{name}@defult.ru', password='1234567890')
        # call_command("createsuperuser",username='default_admin')
