from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from pytils import slugify
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.models import Category, Sneakers, Blog


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

    fields = ('name', 'description',)
    success_url = reverse_lazy('catalog:categories')


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, *kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog

    fields = ('header', 'content',)
    success_url = reverse_lazy('catalog:create_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog

    fields = ('header', 'content', 'photo')
    success_url = reverse_lazy('catalog:update_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:view_blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog

    fields = ('header', 'content', 'photo')
    success_url = reverse_lazy('catalog:delete_blog')



