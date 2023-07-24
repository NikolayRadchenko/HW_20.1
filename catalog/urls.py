from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, categories, sneakers, sneakers_id

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', categories, name='categories'),
    path('snikkers/', sneakers, name='sneakers'),
    path('snikkers/<int:sneakers_id>', sneakers_id, name='sneakers_id'),
]
