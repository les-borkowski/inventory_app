from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    path('', views.list, name='list'),
    path('items/<int:item_id>/', views.detail, name='detail'),
    path('update/<int:item_id>/', views.update, name='update'),
    path('delete/<int:item_id>/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
]   