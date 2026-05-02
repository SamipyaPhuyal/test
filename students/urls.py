from django.contrib import admin
from django.urls import path
from .views import StudentListView
urlpatterns = [
    path("list/",StudentListView.as_view(),name="list-create")
]
