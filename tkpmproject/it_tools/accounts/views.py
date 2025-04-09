from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return HttpResponse("Signing up...")

def login(request):
    return HttpResponse("Logging in...")