from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from models import User


class UserListView(ListView):
    queryset = User.objects.all()

    def get_template_names(self):
        return ['users/user_list.html']


class UserDetailView(DetailView):
    queryset = User.objects.all()
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_template_names(self):
        return ['users/user_detail.html']
