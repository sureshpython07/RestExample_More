from django.urls import path
from app_drf import views
urlpatterns = [
    path('', views.index, name='index'),
]
