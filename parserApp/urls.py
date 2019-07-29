from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_site', views.add_site, name='add_site'),
    path('edit_site', views.edit_site, name='edit_site'),
    path('view_result', views.view_result, name='view_result'),
    path('change', views.change, name='change'),

]
