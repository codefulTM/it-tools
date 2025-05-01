from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool26(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(26)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 26,
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 26")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>
            <p class="tool-des">{self.description}</p>

            <div class="tool-body website-load-time-tester-container">
                <label class="normal-label-down">URL:</label>
                <input class="normal-input" type="text" name="url" required placeholder="Enter URL here...">

                <label class="normal-label-down">Load time (seconds):</label>
                <input class="normal-input" type="number" name="load-time" readonly step="0.001" min="0">

                <label class="normal-label-down">Page size (MB):</label>
                <input class="normal-input" type="number" name="page-size" readonly>

                <label class="normal-label-down">Requests:</label>
                <input class="normal-input" type="number" name="requests" readonly>
            </div>
            <button type="submit" class="normal-btn">Start Test</button>
        """
    
    def get_js(self):
        return """
            
        """
    
    def get_package(self):
        return ""