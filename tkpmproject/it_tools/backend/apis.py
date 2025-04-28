from django.urls import path
from .views import api_tools

urlpatterns = [
    path('tools/', api_tools.get_tools, name="api_tools"),
]