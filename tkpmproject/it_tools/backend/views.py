from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
import bcrypt
from backend.decorators import login_required
from backend.classes.User import *
# from data_service.services.user_services import *
# from data_service.services.user_role_services import *
from data_service.services.tool_services import *
from data_service.services.tool_category_services import *

# Create your views here.

def signup(request):    
    if(request.method == 'POST'):
        # Get username, email and password
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        guest_user = GuestUser()
        result = guest_user.sign_up(email, username, password)

        # Failed to sign up
        if result[0] == False:
            return render(request, 'signup.html', {'message': result[1]})

        return render(request, 'signup.html', {'message': result[1]})
    else:
        return render(request, 'signup.html')
    
def login(request):
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        guest_user = GuestUser()
        result = guest_user.sign_in(username, password)

        # Failed to sign in
        if result[0] == False:
            return render(request, 'login.html', {'message': result[1]})

        # Sign in successfully
        user = result[2]

        # Add login information to request session
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        request.session['user_role'] = user.role

        # Redirect to home page
        return redirect('it_tools')
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
    # Get all it tools
    it_tools = get_all_tools()
    # Convert query set to a list of objects
    it_tools_list = list(it_tools)
    
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
        'it_tools': it_tools_list,
        'user_id': user_id,
        'username': username,
        'user_role': user_role,
        'tool_categories': tool_categories
    }

    return render(request, 'it_tools.html', context)