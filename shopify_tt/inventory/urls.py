from django.urls import path

from . import views

urlpatterns = [
    # ex: /items/
    path('', views.index, name='index'),
    # ex. /items/4/
    path('<int:item_id>/', views.detail, name='detail')
]