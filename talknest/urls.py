from django.urls import path
from talknest.views import home

urlpatterns = [
    path('', home, name='home'),
]
