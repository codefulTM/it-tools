from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool22(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(22)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 22,
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 22")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>
            <p class="tool-des">{self.description}</p>

            <div class="tool-body text-difference-checker-container">
                <label class="normal-label-down">File 1:</label>
                <input class="normal-input" type="file" name="file1" id="file1" accept=".txt">

                <label class="normal-label"></label>
                <textarea class="normal-input" name="text1" rows="5" id="text1" placeholder="Or paste text here..."></textarea>

                <label class="normal-label-down">File 2:</label>
                <input class="normal-input" type="file" name="file2" id="file2" accept=".txt"> 

                <label class="normal-label"></label>
                <textarea class="normal-input" name="text2" rows="5" id="text2" placeholder="Or paste text here..."></textarea>

                <label class="normal-label">Result:</label>
                <div id="result"></div>
            </div>
            <span>
                <input type="button" value="Check Difference" class="normal-btn" id="check-difference">
            </span>
        """
    
    def get_js(self):
        return """
            const fileInput1 = document.getElementById('file1');
            const fileInput2 = document.getElementById('file2');
            const textArea1 = document.getElementById('text1');
            const textArea2 = document.getElementById('text2');
            const resultDiv = document.getElementById('result');
            const checkDiffButton = document.getElementById('check-difference');

            fileInput1.addEventListener('change', readFile, false);

            fileInput2.addEventListener('change', readFile, false);

            textArea1.addEventListener('input', () => {
                if (textArea1.value.trim() !== '') {
                    fileInput1.value = ''; 
                }
            });

            textArea2.addEventListener('input', () => {
                if (textArea2.value.trim() !== '') {
                    fileInput2.value = '';
                }
            });

            checkDiffButton.addEventListener('click', () => {
                const text1 = textArea1.value;
                const text2 = textArea2.value;

                if (text1 == '' || text2 == '') {
                    alert ('Please paste your text or choose a file first!');
                    return;
                }

                const diff = Diff.diffWordsWithSpace(text1, text2);
                resultDiv.innerHTML = '';

                diff.forEach((part) => {
                    let safeText = part.value
                        .replace(/&/g, '&amp;')
                        .replace(/</g, '&lt;')
                        .replace(/>/g, '&gt;')
                        .replace(/\\n/g, '<br>');

                    const span = document.createElement('span');
                    span.style.fontSize = '24px';
                    span.innerHTML = safeText;

                    if (part.added) {
                        span.style.backgroundColor = 'lightgreen';
                    } else if (part.removed) {
                        span.style.backgroundColor = 'lightcoral';
                    }

                    resultDiv.appendChild(span);
                });
            });

            function readFile(event) {
                const file = event.target.files[0];
                if (!file) {
                    showMessage("No file selected. Please choose a file.", "error");
                    return;
                }
                const reader = new FileReader();
                reader.onload = function (readEvent) {
                    let fileContent = readEvent.target.result;
                    console.log(fileContent); 

                    if (event.target.id === 'file1')
                        textArea1.value = fileContent;
                    else if (event.target.id === 'file2')
                        textArea2.value = fileContent;
                };
                reader.onerror = function () {
                    showMessage("Error reading the file. Please try again.", "error");
                };
                reader.readAsText(file);
            }
        """
    
    def get_package(self):
        return "https://cdnjs.cloudflare.com/ajax/libs/jsdiff/7.0.0/diff.min.js"