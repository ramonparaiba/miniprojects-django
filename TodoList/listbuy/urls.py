from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('edit/<int:item_id>/', views.edit_item, name="edit_item"),
    path('delete/<int:item_id>/', views.delete_item, name = 'delete_item')
]
