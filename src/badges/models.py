from django.db.models import Model, OneToOneField
from django.contrib.auth.models import User


class Star(Model):
    user = OneToOneField(User, primary_key=True)


class Collector(Model):
    user = OneToOneField(User, primary_key=True)


class Pioneer(Model):
    user = OneToOneField(User, primary_key=True)


class Heavyweight(Model):
    user = OneToOneField(User, primary_key=True)
