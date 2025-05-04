from django.shortcuts import redirect, render
from data_service.services.tool_category_services import *
from data_service.services.tool_services import *
from data_service.services.user_services import *

def it_tools(request):
    # Get user information 
    user_id = request.session.get('user_id')
    user = get_user_by_id(user_id)

    # Get a list of all categories    
    it_tool_categories = list(get_all_tool_categories())

    context = {
        'user_id': user_id,
        'username': user.username,
        'user_role': user.role.role,
        'it_tool_categories': it_tool_categories
    }

    return render(request, 'it_tools.html', context)

def it_tools_by_category(request, category_id):
    # Get user information in session
    user_id = request.session.get('user_id')
    user = get_user_by_id(user_id)
    
    # Get a list of all categories
    it_tool_categories = list(get_all_tool_categories())

    # Get the information of the category to display
    category = None
    for cat in it_tool_categories:
        if cat.id == category_id:
            category = cat
            break

    context = {
        'user_id': user_id,
        'username': user.username,
        'user_role': user.role.role,
        'it_tool_categories': it_tool_categories,
        'category': category
    }

    return render(request, 'it_tools_by_category.html', context)

def use_tool(request, tool_id):
    # Get user information in session
    user_id= request.session.get('user_id')
    user = get_user_by_id(user_id)

    # Get the tool by id
    tool = get_tool_by_id(tool_id)
    
    # Get a list of all categories
    it_tool_categories = list(get_all_tool_categories())

    context = {
        'user_id': user_id,
        'username': user.username,
        'user_role': user.role.role,
        'it_tool_categories': it_tool_categories,
        'message': None
    }

    # Check if the tool is disabled
    if tool.is_enabled == False:
        context['message'] = 'The tool you are trying to use is disabled.'
        return render(request, 'it_tools.html', context)

    # Check if the tool is premium
    if tool.is_premium == True and user.role.role == 'regular':
        context['message'] = 'The tool you are trying to use is premium and you are not a premium user.'
        return render(request, 'it_tools.html', context)

    context['tool_id'] = tool_id

    return render(request, 'use_tool.html', context)

def favorite_tools(request):
    user_id = request.session.get('user_id')
    user = get_user_by_id(user_id)

    it_tool_categories = list(get_all_tool_categories())

    context = {
        'user_id': user_id,
        'username': user.username,
        'user_role': user.role.role,
        'it_tool_categories': it_tool_categories
    }

    return render(request, 'favorite_tools.html', context)
