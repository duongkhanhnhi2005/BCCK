<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
=======
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
<<<<<<< HEAD
    path('profile/', views.profile_view, name='profile'),

=======
>>>>>>> 799ec24df183f2f18879d711b342b89122e2ec49
>>>>>>> c5ceb21c234907d0bf80c8afcba2fd35dbbe6fb2
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)