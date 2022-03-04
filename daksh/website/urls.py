from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('<int:detail_id>/',views.details,name="detail"),
    path('salary/',views.salary,name="salary"),
    path('salary/analytics/',views.analytics,name="analytics"),
    path('api/v1/',views.v1_api,name="v1_api")
]
