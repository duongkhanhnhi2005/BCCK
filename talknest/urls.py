from django.urls import path,include
from talknest.views import home
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('accounts/', include('allauth.urls')),
    path('login/', views.login, name='login'),
    path('profile/', views.profile_view, name='profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)