from django.http import JsonResponse
from data_service.services.user_role_services import * 
from data_service.services.user_services import * 
from ..utils import *

def get_premium(request):
    user_id, username, user_role = get_user_from_session(request)
    
    user = get_user_by_id(user_id)

    if user.is_premium == True:
        return JsonResponse({'success': False, 'message': 'You are already a premium user.'})

    user.is_premium = True
    user.save()

    return JsonResponse({'success': True, 'message': 'You are now a premium user.'})