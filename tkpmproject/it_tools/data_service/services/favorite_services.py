from data_service.models import Favorite
from data_service.services.tool_services import get_tool_by_id
from data_service.services.user_services import get_user_by_id

# Check favorite tool exist:
def check_favorite_tool(user_id, tool_id):
    try:
        return Favorite.objects.get(user=user_id, tool=tool_id)
    except Favorite.DoesNotExist:
        return None   

# Add a favorite tool from user
def toggle_favorite_tool(user_id, tool_id):
    favorite = check_favorite_tool(user_id, tool_id)
    try:
        if (favorite == None):
            user = get_user_by_id(user_id)
            tool = get_tool_by_id(tool_id)
            favorite = Favorite(user=user, tool=tool)
            favorite.save()
        else:
            favorite.delete()
            
        return True
    except Exception as e:
        print(e)
        return False
        
# Get all favorite tools from user
def get_all_favorite_tools(user_id):
    try:
        favorites = Favorite.objects.filter(user=user_id)
        return favorites    
    except Favorite.DoesNotExist:
        return None
