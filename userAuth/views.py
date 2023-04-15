from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("hi m RUmmmm")

def view_name(request):
    return render(request, 'template_name.html', {})