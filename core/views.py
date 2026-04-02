from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import KeyVal


def index(request: HttpRequest) -> HttpResponse:
    items = KeyVal.objects.all()
    return render(request, "core/index.html", {"items": items})
