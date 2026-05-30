from django.urls import path, include
from core import urls as core_urls

urlpatterns = [
    path("core/", include(core_urls)),
]
