
# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the home page.")
def hello(request):
    return HttpResponse("anushka yadav")
def anshita(request):
    return HttpResponse("anshita rajput")