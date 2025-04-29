from django.urls import path
from .views import api_tools

urlpatterns = [
    path('tools/', api_tools.get_tools, name="api_tools"),
    path('tools/<int:tool_id>/', api_tools.get_one_tool, name="api_tool"),
]