from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('all_news', views.all_news, name = 'all-news'),
    path('detail/<int:id>', views.detail, name ='detail'),
    path('accounts/register/', views.register, name = 'register'),
    path('create', views.create_news, name ='create'),
    path('edit/<int:id>', views.edit, name ='edit'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
