from django.urls import path
from talknest.views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('search/', views.search, name='search'),
]
