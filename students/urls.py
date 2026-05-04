from django.contrib import admin
from django.urls import path,include
from .views import StudentListView,StudentDetailView,StudentSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("student",StudentSet,basename="student")
urlpatterns = [
    path("list/",StudentListView.as_view(),name="list-create"),
    path("list/<int:pk>/",StudentDetailView.as_view(),name="detail"),
    path("newlist/",include(router.urls))
]
