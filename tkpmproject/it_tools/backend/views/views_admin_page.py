from django.shortcuts import redirect, render
from backend.classes.ToolManager import *
from data_service.services.tool_category_services import get_all_tool_categories
from data_service.services.user_services import *
from data_service.services.tool_category_services import *

def get_context(request):
     # Get user information in session
    user_id = None
    username = None
    user_role = None
    it_tool_categories = list(get_all_tool_categories())
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        username = request.session.get('username')
        user_role = request.session.get('user_role')

    context = {
        'user_id': user_id,
        'username': username,
        'user_role': user_role,
        'it_tool_categories': it_tool_categories

def manage_tools(request):
    # Get user information
    user_id = request.session.get('user_id')
    user = get_user_by_id(user_id)

    # Get a list of all categories
    it_tool_categories = list(get_all_tool_categories())

    context = {
        'user_id': user_id,
        'username': user.username,
        'user_role': user.role.role,
        'it_tool_categories': it_tool_categories,
    }

    return context

def manage_tools(request):
    context = get_context(request)

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
    
def enable_and_disable_tool(request):
    context = get_context(request)

    return render(request, 'enable_and_disable_tool.html', context)

def toggle_premium_tool(request):
    context = get_context(request)

    return render(request, 'toggle_premium.html', context)

def remove_tool(request):
    context = get_context(request)

    return render(request, 'remove_tool.html', context)