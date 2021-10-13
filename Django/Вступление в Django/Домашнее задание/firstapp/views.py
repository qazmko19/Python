from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def hello_django(request: HttpRequest):
    print(request.user)
    return HttpResponse("Hello Django!")
