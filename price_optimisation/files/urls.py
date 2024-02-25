from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('custom/', views.custom, name='custom'),
]
