# contact/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('contactlist/', views.contactlist_view, name='contactlist_view'),
]
