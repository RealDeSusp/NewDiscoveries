from django.urls import path

from core.views import get_objects_list

urlpatterns = [
    path("objects/", get_objects_list, name="get_objects_list"),
]
