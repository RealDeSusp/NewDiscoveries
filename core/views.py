import requests
from django.shortcuts import render

from core.enums import BASE_URL


def get_objects_list(request):
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()

    objects = response.json()

    return render(
        request,
        "objects_list.html",
        {"objects": objects},
    )
