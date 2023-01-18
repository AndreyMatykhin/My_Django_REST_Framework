import os
from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from authapp.models import CustomUser


class Project(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    project_name = models.CharField(_("project_name"), max_length=150)
    project_repo = models.FileField(_("Project repositories"), max_length=150, blank=True)
    users_list = models.ManyToManyField(CustomUser)
    create_time = models.DateTimeField(_("Created"), auto_now_add=True)
    status_complete = models.BooleanField(_("Status complete"), default=False)

    def complete(self):
        self.status_complete = True
        self.save()

    def __str__(self) -> str:
        return f"Project '{self.project_name}' - {'complete' if self.status_complete else 'no complete'}"
