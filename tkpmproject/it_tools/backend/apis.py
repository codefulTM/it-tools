from django.urls import path
from .views import api_tools

urlpatterns = [
    path('tools/', api_tools.get_tools, name="api_tools"),
    path('categories/<int:category_id>/', api_tools.get_tools_by_category, name="api_get_tools_by_category"),
    path('tools/<int:tool_id>/', api_tools.get_one_tool, name="api_tool")
]