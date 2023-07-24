from django.shortcuts import render

from catalog.models import Category, Product


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


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Sneakers - Категории'
    }
    return render(request, 'catalog/categories.html', context)


def sneakers(request):
    context = {
        'object_list': Product.objects.filter(category_id=Category.objects.filter(name='Кроссовки').get().id),
        'title': 'Sneakers - Кроссовки'
    }
    return render(request, 'catalog/sneakers.html', context)


def sneakers_id(request, sneakers_id=1):
    context = {
        'object': Product.objects.filter(category_id=Category.objects.filter(name='Кроссовки').get().id),
        'id': Product.objects.filter(id=request.get(id)).get().id,
        'title': f'Sneakers - {Product.objects.filter(id=request.get(id)).get().name}'
    }
    sneakers_id = Product.objects.filter(id=request.get(id)).get().id
    return render(request, 'catalog/sneakers.html', context)
