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