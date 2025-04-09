from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def signup(request):    
    if(request.method == 'POST'):
        # Get username, email and password
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
    return render(request, 'signup.html')
    
def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())