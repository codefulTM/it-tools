from django.http import JsonResponse
from data_service.services.tool_services import *  # assuming this is the model for tools
from backend.classes.ToolManager import ToolManager

def get_tools(request):
    """
    API endpoint to get a list of tools.
    """
    tools = get_all_tools()
    data = []
    for tool in tools:
        data.append({
            'id': tool.id,
            'name': tool.name,
            'description': tool.description,
            'is_enabled': tool.is_enabled,
            'is_premium': tool.is_premium
        })
    return JsonResponse(data, safe=False)

def get_tools_by_category(request, category_id):
    tools = get_all_tools()
    data = []
    for tool in tools:
        if tool.category.id == category_id:
            data.append({
                'id': tool.id,
                'name': tool.name,
                'description': tool.description
            })
    return JsonResponse(data, safe=False)

def get_one_tool(request, tool_id):
    tool_manager = ToolManager()
    tool = tool_manager.get_tool(tool_id)
    data = tool.get_info()
    data['html'] = tool.get_html()
    data['js'] = tool.get_js()
    return JsonResponse(data)

def toggle_tool_status(request, tool_id):
    try:
        tool_manager = ToolManager()
        if (tool_manager.toggle_enable(tool_id)):
            return JsonResponse({"success": True, "message": "Tool status updated successfully."})
        else:    
            return JsonResponse({"success": False, "message": "Tool status updated unsuccessfully."})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})