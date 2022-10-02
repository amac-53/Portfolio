from turtle import clearstamps
from django.urls import path, include
from .views import IndexView, DetailView, AboutView, ContactView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact')
]
