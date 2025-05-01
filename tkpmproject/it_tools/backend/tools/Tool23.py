from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool23(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(23)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 23,
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 23")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>

            <p class="tool-des">{self.description}</p>

            <div class="tool-body text-statistics-container">
                <label class="normal-label-down">File:</label>
                <input class="normal-input" type="file" accept=".txt" name="file" id="file">
                
                <label class="normal-label">Text:</label>
                <textarea class="normal-input" name="text" rows="10" id="text" placeholder="Or paste text here..." required></textarea>

                <label class="normal-label-down">Characters:</label>
                <input class="normal-input" type="number" name="characters" id="characters" value="0" readonly>

                <label class="normal-label-down">Words:</label>
                <input class="normal-input" type="number" name="words" id="words" value="0" readonly>

                <label class="normal-label-down">Lines:</label>
                <input class="normal-input" type="number" name="lines" id="lines" value="0" readonly>

                <label class="normal-label-down">Size (Bytes):</label>
                <input class="normal-input" type="number" name="size" id="size" value="0" readonly>
            </div>
        """
    
    def get_js(self):
        return """
            const fileInput = document.getElementById('file');
            const textArea = document.getElementById('text');
            const charsCount = document.getElementById('characters');
            const wordsCount = document.getElementById('words');
            const linesCount = document.getElementById('lines');
            const sizeCount = document.getElementById('size');

            fileInput.addEventListener('change', () => {
                if (fileInput.files.length > 0) {
                    const file = fileInput.files[0];
                    if (!file) {
                        showMessage("No file selected. Please choose a file.", "error");
                        return;
                    }
                    const reader = new FileReader();
                    reader.onload = function (readEvent) {
                        let fileContent = readEvent.target.result;
                        textArea.value = fileContent;
                        sizeCount.value = file.size;
                        updateStatistics();

                        console.log(fileContent); 
                    };
                    reader.onerror = function () {
                        showMessage("Error reading the file. Please try again.", "error");
                    };
                    reader.readAsText(file);
                }
            });

            textArea.addEventListener('change', () => {
                fileInput.value = '';
                updateStatistics();
            });

            function updateStatistics() {
                const text = textArea.value;

                if (text == '') {
                    charsCount.value = 0;
                    wordsCount.value = 0;
                    linesCount.value = 0;
                    sizeCount.value = 0;
                    return;
                }

                charsCount.value = text.replace(/\s/g, '').length;
                wordsCount.value = text.match(/\S+/g).length;
                linesCount.value = text.split(/\\n/).length;
                if (fileInput.value == '')
                    sizeCount.value = (new Blob([text])).size;
            }
        """
    
    def get_package(self):
        return ""