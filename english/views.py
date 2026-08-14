from django.shortcuts import render
from django.http import HttpRequest



def luminaria(request: HttpRequest):
    return render(request, "index.html")