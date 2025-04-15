from django.shortcuts import redirect, render
from data_service.services.user_role_services import *

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'user_id' in request.session:
            return view_func(request, *args, **kwargs)
        return redirect('login')
    return wrapper

def premium_user_required(view_func):
    def wrapper(request, *args, **kwargs):
        role_id = request.session.get('user_role')
        user_role = get_user_role_by_name('premium')
        if role_id == user_role.id:
            return view_func(request, *args, **kwargs) 
        return redirect('/')
    return wrapper

def admin_user_required(view_func):
    def wrapper(request, *args, **kwargs):
        role_id = request.session.get('user_role')
        user_role = get_user_role_by_name('admin')
        if role_id == user_role.id:
            return view_func(request, *args, **kwargs) 
        return redirect('/')
    return wrapper