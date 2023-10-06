from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from catalog.forms import SneakersForm
from catalog.models import Category, Sneakers


def home(request):
    context = {
        'object_list': Category.objects.all()[:3],
        'title': 'Sneakers - Ваш стиль'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    return render(request, 'catalog/contacts.html')


class CategoryListView(ListView):
    model = Category

    extra_context = {
        'title': 'Sneakers - Категории'
    }


class SneakersListView(ListView):
    model = Sneakers

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=Category.objects.filter(name='Кроссовки').get().id)
        return queryset

    extra_context = {
        'title': 'Sneakers - Кроссовки'
    }


class SneakersCreateView(CreateView):
    model = Sneakers
    form_class = SneakersForm
    success_url = reverse_lazy('catalog:categories')


class SneakersUpdateView(UpdateView):
    model = Sneakers
    form_class = SneakersForm
    success_url = reverse_lazy('catalog:categories')
