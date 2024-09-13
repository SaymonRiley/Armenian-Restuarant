from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),  # No slug here
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.main, name='category_detail'),  # This should be last to avoid conflicts
]
