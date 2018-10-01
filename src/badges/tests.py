from datetime import timedelta

from django.utils import timezone
from django.test import TestCase

from users.models import User
from models3d.models import Model
from .models import Star, Collector, Pioneer, Heavyweight


class BadgeTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='password',
            date_joined=timezone.now() - timedelta(days=365),
        )

    def test_star(self):
        model = Model.objects.create(user=self.user, name='cube')

        for _ in range(100):
            self.client.get('/models/' + model.name)

        self.assertTrue(Star.objects.filter(user=self.user))

    def test_collector(self):
        self.client.login(username=self.user.username, password='password')

        for _ in range(5):
            with open('data/tests/triangle.obj') as fd:
                self.client.post('/models', data={'file': fd})

        self.assertTrue(Collector.objects.filter(user=self.user))

    def test_pioneer(self):
        self.client.login(username=self.user.username, password='password')
        self.assertTrue(Pioneer.objects.filter(user=self.user))

    def test_heavyweight(self):
        self.client.login(username=self.user.username, password='password')

        with open('data/tests/big_triangle.obj') as fd:
            self.client.post('/models', data={'file': fd})

        self.assertTrue(Heavyweight.objects.filter(user=self.user))
