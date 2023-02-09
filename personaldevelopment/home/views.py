
# Create your views here.
from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "index.html")
def hello(request):
    return HttpResponse("anushka yadav")
def anshita(request):
    return HttpResponse("anshita rajput")