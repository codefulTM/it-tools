from django.http import JsonResponse
from data_service.services.tool_services import *  # assuming this is the model for tools

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

