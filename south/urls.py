from django.urls import path
from . import views

urlpatterns = [
    path('rus', views.ru, name='rus'),
    path('ua', views.ukr, name='ukr'),
    path('', views.ru, name='rus'),

]
