from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, CategoryListView, SneakersListView, SneakersCreateView, SneakersUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('sneakers/', SneakersListView.as_view(), name='sneakers'),
    path('sneakers/create', SneakersCreateView.as_view(), name='sneakers_create'),
    path('sneakers/update/<int:pk>', SneakersUpdateView.as_view(), name='update_sneakers'),
]
