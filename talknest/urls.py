from django.urls import path,include
from talknest.views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login, name='login'),
    path('communities/', views.community_list, name='community_list'),
    path('communities/create/', views.create_community, name='create_community'),
    path('communities/<int:community_id>/', views.community_detail, name='community_detail'),
]
