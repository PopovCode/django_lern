from django.urls import path

from . import views


app_name = 'tovar'
urlpatterns = [
    path('', views.index, name='index'),
]