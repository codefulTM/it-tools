from django.http import JsonResponse
from data_service.services.user_role_services import * 
from data_service.services.user_services import * 
from ..utils import *

def get_premium(request, user_id):
    user = get_user_by_id(user_id)

    if user == None:
        return JsonResponse({'success': False, 'message': 'User does not exist.'})

    if user.role.role == 'premium' or user.role.role == 'admin':
        return JsonResponse({'success': False, 'message': 'You are already a premium or an admin user.'})

    user.role = get_user_role_by_name('premium')
    user.save()
    request.session['user_role'] = user.role.role

    return JsonResponse({'success': True, 'message': 'You are now a premium user.'})