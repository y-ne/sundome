from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import KeyVal


def index(request: HttpRequest) -> HttpResponse:
    items = KeyVal.objects.all()
    return render(request, "core/index.html", {"items": items})


def detail(request: HttpRequest, pk: int) -> HttpResponse:
    item = get_object_or_404(KeyVal, pk=pk)
    return render(request, "core/detail.html", {"item": item})


def add(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        key = request.POST.get("key", "")
        value = request.POST.get("value", "")

        if not key:
            return render(request, "core/add.html", {"err_msg": "key is required"})

        KeyVal.objects.create(key=key, value=value)
        return HttpResponseRedirect(reverse("core:index"))
    return render(request, "core/add.html")
