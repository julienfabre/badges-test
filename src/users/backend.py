from datetime import timedelta

from django.utils import timezone
from django.contrib.auth.backends import ModelBackend
from django.apps import apps

CONST_PIONEER = 365


class CustomBackend(ModelBackend):
    """
    Custom Backend to award Pioneer badge at User login.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        """
        Overriding authenticate method from ModelBackend (standard Django authentication backend)
        to award Pioneer badge at User login.
        """
        user = super(CustomBackend, self).authenticate(username, password, **kwargs)

        # Lazy loading Pioneer model to avoid circular imports.
        pioneer_model = apps.get_model(app_label="badges", model_name="Pioneer")

        if (user.date_joined < timezone.now() - timedelta(days=CONST_PIONEER)) and \
                not pioneer_model.objects.filter(user=user).exists():
            # Awarding Pioneer badge.
            pioneer_model.objects.create(user=user)

        return user
