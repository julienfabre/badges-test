
from django.contrib.auth.models import AbstractUser

from managers import SketchfabUserManager


class User(AbstractUser):
    """
    Custom User model.
    See:
    https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
    """
    objects = SketchfabUserManager()
