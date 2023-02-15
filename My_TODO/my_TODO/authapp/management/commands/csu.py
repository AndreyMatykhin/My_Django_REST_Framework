from django.core.management.base import BaseCommand
from authapp.models import CustomUser


class Command(BaseCommand):
    help = 'Создает случайного суперпользователя'

    def handle(self, *args, **kwargs):
        CustomUser.objects.create_superuser(username='admin', email=f'admin@defult.ru', password='a12')
