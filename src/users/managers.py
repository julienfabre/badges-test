from datetime import timedelta

from django.utils import timezone
from django.contrib.auth.models import UserManager

import badges


class SketchfabUserManager(UserManager):
    def get(self, *args, **kwargs):
        """
        Overriding get method to award Pioneer badge at login.
        """
        user = super(UserManager, self).get(*args, **kwargs)
        if (user.date_joined < timezone.now() - timedelta(days=365)) and user.pioneer.count() == 0:
            pioneer = badges.models.Pioneer()
            pioneer.user = user
            pioneer.save()
        return user