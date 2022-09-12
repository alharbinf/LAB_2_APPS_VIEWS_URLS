from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("home/", views.my_fun, name="my_fun")
]
