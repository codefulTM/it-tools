from django.urls import path
from .views import api_tools

urlpatterns = [
    path('tools/', api_tools.get_tools, name="api_tools"),
    path('categories/<int:category_id>/', api_tools.get_tools_by_category, name="api_get_tools_by_category"),
    path('favorites/toggle/<int:user_id>/<int:tool_id>/', api_tools.toggle_favorite_tool, name="api_toggle_favorite_tool"),
    path('favorites/<int:user_id>/', api_tools.get_all_favorites, name="api_get_all_favorites"),
    path('tools/<int:tool_id>/toggleenable/', api_tools.toggle_tool_status, name="api_toggle_tool_status"),
    path('tools/<int:tool_id>/togglepremium/', api_tools.toggle_tool_premium, name="api_toggle_tool_premium"),
    path('tools/<int:tool_id>/deletetool/', api_tools.delete_tool, name="api_delete_tool"),
    path('tools/<int:tool_id>/', api_tools.get_one_tool, name="api_tool")
]