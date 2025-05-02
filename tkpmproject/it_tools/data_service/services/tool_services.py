from data_service.models import Tool
from . import tool_category_services

# Get all function
def get_all_tools():
    return Tool.objects.all()

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

# Toggle enable/disable tool
def toggle_enable_tool(tool_id):
    tool = get_tool_by_id(tool_id)
    if (tool != None):
        tool.is_enabled = not tool.is_enabled
        tool.save()
        return True
    else:
        return False
    
# Toggle premium tool
def toggle_premium_tool(tool_id):
    tool = get_tool_by_id(tool_id)
    if (tool != None):
        tool.is_premium = not tool.is_premium
        tool.save()
        return True
    else:
        return False