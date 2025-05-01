from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool29(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(29)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 29,
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 29")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>
            <p class="tool-des">{self.description}</p>

            <div class="tool-body json-formatting-container">
                <label class="normal-label-down">Paste the JSON file:</label>
                <input class="normal-input" type="file" name="file" id="file" accept=".txt,.json">

                <label class="normal-label">Current JSON content:</label>
                <textarea class="normal-input" name="text" rows="10" id="text" placeholder="Or paste the JSON code here..." required></textarea>

                <label class="normal-label-down">Formated JSON code:</label>
                <textarea class="normal-input" name="formatted-text" rows="10" id="formatted-text" placeholder="Formatted code goes here..." readonly></textarea>
            </div>
            <input type="button" value="Format JSON code" class="normal-btn" id="format-json">
            <input type="button" value="Download JSON code" class="normal-btn" id="download-json">
        """
    
    def get_js(self):
        return """
            const fileInput = document.getElementById("file");
            const textInput = document.getElementById("text");
            const formattedJSON = document.getElementById("formatted-text");
            const formatJSON = document.getElementById("format-json");
            const downloadJSON = document.getElementById("download-json");

            fileInput.addEventListener("change", () => {
                if (fileInput.files.length > 0) {
                    const file = fileInput.files[0];
                    if (!file) {
                        showMessage("No file selected. Please choose a file.", "error");
                        return;
                    }
                    const reader = new FileReader();
                    reader.onload = function (readEvent) {
                        let fileContent = readEvent.target.result;
                        console.log(fileContent); 

                        textInput.value = fileContent;
                    };
                    reader.onerror = function () {
                        showMessage("Error reading the file. Please try again.", "error");
                    };
                    reader.readAsText(file);
                }
            });

            textInput.addEventListener("change", () => {
                if (textInput.value.trim() !== '') {
                    fileInput.value = '';
                }
            });
            
            formatJSON.addEventListener("click", () => {
                if (!textInput || textInput.value == '') {
                    alert ("Please input the JSON content or choose the JSON file first!");
                    return;
                }

                try {
                    const parsed = JSON.parse(textInput.value);
                    const formatted = JSON.stringify(parsed, null, 4);
                    formattedJSON.value = formatted;
                } catch (err) {
                    console.error ("Failed to format JSON content");
                    alert ("Failed to format JSON content");
                }
            });

            downloadJSON.addEventListener("click", () => {
                if (!formattedJSON || formattedJSON.value == '') {
                    alert ("Please format the JSON content first!");
                    return;
                }

                try {
                    const blob = new Blob ([formattedJSON.value], { type: "application/json" });
                    const url = URL.createObjectURL(blob);

                    const a = document.createElement('a');
                    a.href = url;
                    a.download = "formatted.json"; // File name
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);

                    URL.revokeObjectURL(url);
                } catch (err) {
                    console.error ("Failed to download formatted JSON file", err);
                    alert ("Failed to download formatted JSON file");
                }
            });
        """
    
    def get_package(self):
        return ""