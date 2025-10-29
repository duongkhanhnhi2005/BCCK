<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
=======
from django.urls import path,include
from talknest.views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login, name='login'),
>>>>>>> 799ec24df183f2f18879d711b342b89122e2ec49
]
