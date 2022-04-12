from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path('<int:detail_id>/',views.details,name="detail"),
    path('expenses/',views.expenses,name="salary"),
    path('expenses/analytics/',views.analytics,name="analytics"),
    path('api/v1/',views.v1_api,name="v1_api")
]
