from data_service.models import Tool
from . import tool_category_services

# Get all function
def get_all_tools():
    return Tool.objects.all().values().order_by('id')
# Get tool by id function
def get_tool_by_id(tool_id):
    try:
        tool = Tool.objects.get(id=tool_id)
        return tool
    except Tool.DoesNotExist:
        return None
    
# Create tool
def create_tool(name, description, category_name, is_premium, is_enabled):
    category = tool_category_services.get_tool_category_by_name(category_name)
    if not category:
        category = tool_category_services.create_tool_category(category_name)
    try:
        tool = Tool.objects.get(name=name, category=category)
        return tool
    except Tool.DoesNotExist:
        tool = Tool(name=name, description=description, category=category, is_premium=is_premium, is_enabled=is_enabled)
        tool.save()
        return tool
