import os
import importlib
from . import ToolComponent
from data_service.services.tool_services import *

class ToolManager:
    def __init__(self):
        pass
        # self.tools = None

        # # From the files in the "tools" folder, get all the classes that extend the Tool 
        # # class and add objects of those classes to the tools list
        # folder_name = "../tools"
        # for filename in os.listdir(folder_name):
        #     if filename.endswith(".py"):
        #         module_name = filename[:-3]
        #         module_path = f"{folder_name}.{module_name}".replace("/", "")  
        #         module = importlib.import_module(module_path)

        #         for attr_name in dir(module):
        #             attr = getattr(module, attr_name)
        #             if isinstance(attr, type) and issubclass(attr, ToolComponent) and attr is not Tool:
        #                 self.tools.append(attr())

    def get_tool(tool_id):
        module_path = f"..tools.Tool{tool_id}"
        module = importlib.import_module(module_path)
        
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if isinstance(attr, type) and issubclass(attr, ToolComponent) and attr is not Tool:
                return attr()

    def add_tool(self, tool_config, html_content, js_content): 
        # Add the tool's information into the database
        tool = create_tool(tool_config['name'], tool_config['description'], tool_config['category'], tool_config['is_premium'], tool_config['is_enabled'])

        # Create the content of the new file that includes the class that extends the ToolComponent class
        content = f'''
            class Tool{tool.id}(ToolComponent):
                def get_info(self):
                    return {{
                        'id': {tool.id},
                        'name': {tool_config['name']},
                        'description': {tool_config['description']},
                        'category': {tool_config['category']},
                        'is_premium': {tool_config['is_premium']},
                        'is_enabled': {tool_config['is_enabled']}
                    }}

                def get_html(self):
                    return {html_content}
                
                def get_js(self):
                    return {js_content}
        '''

        # Save the content into a file in the tools folder
        dir_path = "../tools"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_path = f"{dir_path}/Tool{tool.id}.py"
        with open(file_path, "w") as file:
            file.write(content)

    def remove_tool(self, tool):
        # Remove the tool's information from the database

        # Remove the file that has the same name as the class name of the tool

        pass