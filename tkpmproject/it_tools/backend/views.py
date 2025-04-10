from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from ..data_service.services.user_services import *

# Create your views here.
def signup(request):    
    if(request.method == 'POST'):
        # Get username, email and password
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        users = get_all_users()
        # Check if the username already exists
        user = users.filter(username=username)
        if user.exists():
            return HttpResponse("Username already exists")
        
        # Check if the email already exists
        user = users.filter(email=email)
        if user.exists():
            return HttpResponse("Email already exists")
        
        # Create user

        # 

    return render(request, 'signup.html')
    
def login(request):
    template = loader.get_template("login.html")
    return HttpResponse(template.render())