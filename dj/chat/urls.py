from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<str:room_name>/', views.room, name='room'),
    path('api/v1/', views.api, name='api'),
    path('push_data_to_redis/', views.push_data_to_redis, name='push_data_to_redis'),
]