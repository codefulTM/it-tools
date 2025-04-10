from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
import bcrypt
from data_service.services.user_services import *
from data_service.services.user_role_services import *

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
            # return HttpResponse("Username already exists")
            return render(request, 'signup.html', {'message': 'Username already exists'})
        # Check if the email already exists
        user = users.filter(email=email)
        if user.exists():
            # return HttpResponse("Email already exists")
            return render(request, 'signup.html', {'message': 'Email already exists'})
        
        user_roles = get_all_user_roles()
        
        # Create user
        if email == 'ntminh22@clc.fitus.edu.vn':    
            user_role = get_user_role_by_name('admin')
            user = create_user(username, email, password, user_role)
        else:
            user_role = get_user_role_by_name('regular')
            user = create_user(username, email, password, user_role)  

        return render(request, 'signup.html', {'message': 'User created successfully'})
    else:
        return render(request, 'signup.html')
    
def login(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Get a list of users
        users = get_all_users()
        # Get the user with the corresponding username
        try:
            user = users.get(username=username)
            if bcrypt.checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
                request.session['user_id'] = user.id
                return HttpResponse("Login successful")
            else:
                return render(request, 'login.html', {'message': 'Invalid password'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'message': 'Username does not exist'})
    else:
        return render(request, 'login.html')