from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Clothe


class ClotheListView(ListView):
    template_name = "clothes/clothe-list.html"
    model = Clothe


class ClotheDetailView(DetailView):
    template_name = "clothes/clothe-detail.html"
    model = Clothe


class ClotheCreateView(CreateView):
    template_name = "clothes/clothe-create.html"
    model = Clothe
    fields = ['name', 'description', 'purchaser']


class ClotheUpdateView(UpdateView):
    template_name = "clothes/clothe-update.html"
    model = Clothe
    fields = ['name', 'description', 'purchaser']


class ClotheDeleteView(DeleteView):
    template_name = "clothes/clothe-delete.html"
    model = Clothe
    success_url = reverse_lazy("clothe_list")