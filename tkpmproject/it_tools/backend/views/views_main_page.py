from django.shortcuts import redirect, render
from backend.utils import get_user_from_session
from data_service.services.tool_category_services import *

def it_tools(request):
    # Get user information in session
    user_id, username, user_role = get_user_from_session(request)
    it_tool_categories = list(get_all_tool_categories())

    context = {
        'user_id': user_id,
        'username': username,
        'user_role': user_role,
        'it_tool_categories': it_tool_categories
    }

    return render(request, 'it_tools.html', context)

def it_tools_by_category(request, category_id):
    # Get user information in session
    user_id, username, user_role = get_user_from_session(request)
    
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
        'username': username,
        'user_role': user_role,
        'it_tool_categories': it_tool_categories,
        'category': category
    }

    return render(request, 'it_tools_by_category.html', context)

def use_tool(request, tool_id):
    # Get user information in session
    user_id, username, user_role = get_user_from_session(request)

    context = {
        'user_id': user_id,
        'username': username,
        'user_role': user_role,
        'tool_id': tool_id
    }

    return render(request, 'use_tool.html', context)