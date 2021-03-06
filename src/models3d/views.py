from django.views.generic.base import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Model
from .forms import ModelCreateForm
from .processing import Processor
from badges.models import Collector, Star, Heavyweight
from users.models import User

CONST_COLLECTOR = 5
CONST_STAR = 100
CONST_HEAVYWEIGHT = 10


class ModelCreateView(CreateView):
    form_class = ModelCreateForm
    model = Model
    success_url = '/'

    def form_valid(self, form):
        model = form.save(commit=False)
        user = User.objects.get(pk=self.request.user.pk)
        model.user = user
        model.save()

        if user.models.count() >= CONST_COLLECTOR and not Collector.objects.filter(user=user).exists():
            # Award Collector badge.
            Collector.objects.create(user=user)

        processor = Processor()
        processor.configure(model.file.path)
        weight = processor.weigh()
        if weight > CONST_HEAVYWEIGHT and not Heavyweight.objects.filter(user=user).exists():
            # Award Heavyweight badge.
            Heavyweight.objects.create(user=user)

        model.weight = weight
        model.vertice_count = processor.count_vertices()
        model.save()

        return super(ModelCreateView, self).form_valid(form)


class ModelListView(ListView):
    queryset = Model.objects.all()


class ModelsView(View):
    def post(self, request, *args, **kwargs):
        return ModelCreateView.as_view()(request)

    def get(self, request, *args, **kwargs):
        return ModelListView.as_view()(request)


class ModelDetailView(DetailView):
    queryset = Model.objects.all()
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_object(self, queryset=None):
        """
        Overriding get_object method from SingleObjectMixin to sum the 3D Model's views.
        """
        model = super(ModelDetailView, self).get_object(queryset=queryset)
        model.viewcount += 1
        model.save()

        if model.viewcount >= CONST_STAR and not Star.objects.filter(user=model.user).exists():
            # Award Star badge.
            Star.objects.create(user=model.user)

        return model
