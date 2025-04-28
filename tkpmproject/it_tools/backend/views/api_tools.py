from django.http import JsonResponse
from data_service.services.tool_services import *  # assuming this is the model for tools

def get_tools(request):
    """
    API endpoint to get a list of tools.
    """
    tools = get_all_tools()
    return JsonResponse(list(tools), safe=False)

