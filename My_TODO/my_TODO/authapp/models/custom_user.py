from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username_validator = ASCIIUsernameValidator()

    class UserCategory(models.TextChoices):
        ADMINISTRATOR = 'AD', _('Administrator')
        MANAGER = 'MG', _('Manager')
        DEVELOPERS = 'DV', _('Developers')

    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(_("username"),
                                max_length=150,
                                unique=True,
                                help_text=_("Required. 150 characters or fewer. ASCII letters and digits only."),
                                validators=[username_validator],
                                error_messages={"unique": _("A user with that username already exists."), },
                                )
    email = models.CharField(_("email address"),
                             max_length=256,
                             unique=True,
                             error_messages={"unique": _("A user with that email address already exists."), },
                             )
    user_category = models.CharField(_("user category"),
                                     max_length=2,
                                     choices=UserCategory.choices,
                                     default=UserCategory.DEVELOPERS,
                                     help_text=_("Defines the category of the project user."),
                                     )
    is_staff = models.BooleanField(_("staff status"),
                                   default=False,
                                   help_text=_("Designates whether the user can log into this admin site."),
                                   )
    is_active = models.BooleanField(_("active"),
                                    default=True,
                                    help_text=_("Designates whether this user should be treated as active. "
                                                "Unselect this instead of deleting accounts."),
                                    )
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True)

    objects = UserManager()

    def is_upperclass(self):
        return self.user_category in {self.UserCategory.ADMINISTRATOR, self.UserCategory.MANAGER, }

    # def _do_update(self, base_qs, using, pk_val, values, update_fields, forced_update):