from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('sat_api/v1/',views.sat_api,name="sat_api"),
    path('test/',views.test,name="test"),
    path('lobby/',views.lobby,name='lobby'),
]
