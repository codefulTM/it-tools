from django.urls import path
from .views import api_tools
from .views import api_users

urlpatterns = [
    path('tools/', api_tools.get_tools, name="api_tools"),
    path('categories/<int:category_id>/', api_tools.get_tools_by_category, name="api_get_tools_by_category"),
    path('tools/<int:tool_id>/', api_tools.get_one_tool, name="api_tool"),
    path('users/getpremium/<int:user_id>/', api_users.get_premium, name="api_get_premium")
]