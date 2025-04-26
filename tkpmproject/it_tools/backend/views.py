from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers
import bcrypt
import json
from backend.decorators import login_required
from data_service.services.user_services import *
from data_service.services.user_role_services import *
from data_service.services.tool_services import *
from data_service.services.tool_category_services import *

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
                request.session['username'] = user.username
                request.session['user_role'] = user.role.role
                return redirect('it_tools')
            else:
                return render(request, 'login.html', {'message': 'Invalid password'})
        except User.DoesNotExist:
            return render(request, 'login.html', {'message': 'Username does not exist'})
    else:
        # If the request session already has login information -> redirect to home page
        if 'user_id' in request.session:
            return redirect('it_tools')
        return render(request, 'login.html')
    
@login_required
def logout(request):
    request.session.flush()
    return redirect('login')

def it_tools(request):
    context = get_master_context(request)
    return render(request, 'it_tools.html', context)

def qr_code_generator_tool(request):
    context = get_master_context(request)
    return render(request, 'tools/qr_code_generator.html', context)

def wifi_qr_code_generator_tool(request):
    context = get_master_context(request)
    return render(request, 'tools/wifi_qr_code_generator.html', context)

def svg_placeholder_generator_tool(request):
    context = get_master_context(request)
    return render(request, 'tools/svg_placeholder_generator.html', context)

def random_prime_generator_tool(request):
    context = get_master_context(request)
    return render(request, 'tools/random_prime_generator.html', context)

def random_name_generator_tool(request):    
    context = get_master_context(request)
    return render(request, 'tools/random_name_generator.html', context)

def random_date_generator_tool(request):
    context = get_master_context(request)
    return render(request, 'tools/random_date_generator.html', context)

def text_difference_checker_tool(request):
    context = get_master_context(request)
    return render(request, 'tools/text_difference_checker.html', context)

def text_statistics_tool(request):
    context = get_master_context(request)
    return render(request, 'tools/text_statistics.html', context)

def lorem_ipsum_generator_tool(request):
    context = get_master_context(request)
    return render(request, 'tools/lorem_ipsum_generator.html', context)

def get_master_context(request):
    # Get all it tools and convert query set to a list of objects
    it_tools = json.dumps(list(get_all_tools()), default=str)
    
    # Get user information in session
    user_id = None
    username = None
    user_role = None
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        username = request.session.get('username')
        user_role = request.session.get('user_role')

    # Get all tool categories
    tool_categories = list(get_all_tool_categories())

    context = {
        'it_tools': it_tools,
        'user_id': user_id,
        'username': username,
        'user_role': user_role,
        'tool_categories': tool_categories
    }
    return context