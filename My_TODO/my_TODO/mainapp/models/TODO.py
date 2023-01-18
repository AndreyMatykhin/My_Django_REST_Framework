from django.db import models
from django.utils.translation import gettext_lazy as _
from mainapp.models import Project
from authapp.models import CustomUser
from django.contrib.auth import get_user_model


class TODO(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    users_list = models.ManyToManyField(CustomUser, default=get_user_model())
    created = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)
    updated = models.DateTimeField(_("Updated"), auto_now_add=True, editable=False)
    status_complete = models.BooleanField(_("Status complete"), default=False)

    def complete(self):
        self.status_complete = True
        self.save()

    def __str__(self) -> str:
        return f'Note "{self.title}" of Project "{self.project_name}" - {"complete" if self.status_complete else "no complete"}'
