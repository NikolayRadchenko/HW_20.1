from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import home, contacts, CategoryListView, SneakersListView, SneakersCreateView, BlogCreateView, \
    BlogDetailView, BlogUpdateView, BlogDeleteView, BlogListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('sneakers/', SneakersListView.as_view(), name='sneakers'),
    path('sneakers/create', SneakersCreateView.as_view(), name='sneakers_create'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('create/', BlogCreateView.as_view(), name='create_blog'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view_blog'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    # path('sneakers/<int:pk>', sneakers_id, name='sneakers_id'),
]
