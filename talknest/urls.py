from django.urls import path, include
from talknest import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('search_advanced/', views.search_advanced, name='search_advanced'),
    path('register/', views.register, name='register'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login, name='login'),
    path('communities/', views.community_list, name='community_list'),
    path('communities/create/', views.create_community, name='create_community'),
    path('communities/<int:community_id>/', views.community_detail, name='community_detail'),
    path('profile/', views.profile_view, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
