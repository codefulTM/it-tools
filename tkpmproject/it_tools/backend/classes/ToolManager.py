import os
import importlib
from classes.Tool import Tool

class ToolManager:
    def __init__(self):
        self.tools = None

        # From the files in the "tools" folder, get all the classes that extend the Tool 
        # class and add objects of those classes to the tools list
        folder_name = "../tools"
        for filename in os.listdir(folder_name):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module_path = f"{folder_name}.{module_name}".replace("/", "")  
                module = importlib.import_module(module_path)

                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and issubclass(attr, Tool) and attr is not Tool:
                        self.tools.append(attr())
        

    def add_tool(self, tool_config, html_file, js_file):                
        # Get the content of the html_file 
        
        # Get the content of the js_file

        # Create the content of the new file that includes the class that extends the Tool class

        # Add the tool's information into the database, including the class name

        pass

    def remove_tool(self, tool):
        # Remove the tool's information from the database

        # Remove the file that has the same name as the class name of the tool

        pass