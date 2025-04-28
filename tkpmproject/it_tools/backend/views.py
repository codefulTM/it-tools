from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
import bcrypt
from backend.decorators import login_required
from backend.classes.User import *
from backend.classes.ToolManager import *
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

def manage_tools(request):
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

    return render(request, 'manage_tools.html', context)

def add_tool(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        is_premium = 'isPremium' in request.POST

        html_file = request.FILES.get('html_file')
        js_file = request.FILES.get('js_file')

        if not name or not description or not category:
            return render(request, 'add_tool.html', {'message': 'All fields are required.'})

        if html_file:
            html_content = html_file.read().decode('utf-8')
        else:
            html_content = ''

        if js_file:
            js_content = js_file.read().decode('utf-8')
        else:
            js_content = ''

        tool_config = {
            'name': name,
            'description': description,
            'category': category,
            'is_premium': is_premium,
            'is_enabled': True  # Assuming new tools are enabled by default
        }

        tool_manager = ToolManager()
        tool_manager.add_tool(tool_config, html_content, js_content)

        return redirect('manage_tools')
    else:
        return render(request, 'add_tool.html')

