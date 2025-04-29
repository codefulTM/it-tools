from data_service.models import ToolCategory

# Get all function
def get_all_tool_categories():
    return ToolCategory.objects.all().values().order_by('id')

# Get by name function
def get_tool_category_by_name(name):
    try:
        return ToolCategory.objects.get(name=name)
    except ToolCategory.DoesNotExist:
        return None
    
# Get by id function
def get_tool_category_by_id(id):
    try: 
        return ToolCategory.objects.get(id=id)
    except ToolCategory.DoesNotExist:
        return None

# Create tool category
def create_tool_category(name):
    if ToolCategory.objects.filter(name=name).exists():
        return None
    tool_category = ToolCategory(name=name)
    tool_category.save()
    return tool_category
