from datetime import timedelta

from django.utils import timezone
from django.contrib.auth.models import UserManager
from django.apps import apps


class SketchfabUserManager(UserManager):
    def get(self, *args, **kwargs):
        """
        Overriding get method from QuerySet to award Pioneer badge at login.
        """
        user = super(UserManager, self).get(*args, **kwargs)

        # Lazy loading Pioneer model to avoid circular imports.
        pioneer_model = apps.get_model(app_label="badges", model_name="Pioneer")

        if (user.date_joined < timezone.now() - timedelta(days=365)) and \
                not pioneer_model.objects.filter(user=user).exists():
            # Awarding Pioneer badge.
            pioneer_model.objects.create(user=user)

        return user