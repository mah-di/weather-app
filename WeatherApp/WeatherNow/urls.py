from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name='home'),
    path('<city_name>/', views.city_details, name='city_details'),
    path('delete-city/<city>/', views.delete_city, name='delete_city'),
]