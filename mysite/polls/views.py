from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    return HttpResponse('Hello world Django documentation')

    