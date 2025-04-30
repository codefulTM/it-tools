from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool20(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(20)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 20,
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 20")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>
            <p class="tool-des">{self.description}</p>

            <div class="tool-body name-generator-container">
                <label class="normal-label-down">First letter limit:</label>
                <select name="first-letter-limit" class="dropdown" id="first-letter">
                    <option value="from-to" selecteed>From leter to letter</option>
                    <option value="single">Single letter only</option>
                </select>

                <label class="normal-label-down">Length (3 to 8):</label>
                <div class="number-input">
                    <button class="btn decrement" id="decrease-btn">−</button>
                    <input type="number" id="name-length" value="3" required>
                    <button class="btn increment" id="increase-btn">+</button>
                </div>

                <label class="normal-label-down" id="from-label">From:</label>
                <input class="normal-input" type="text" id="from-letter" maxlength="1" pattern="[A-Z]" required>

                <label class="normal-label-down" id="to-label">To:</label>
                <input class="normal-input" type="text" id="to-letter" maxlength="1" pattern="[A-Z]" required>

                <label class="normal-label-down" id="single-label" hidden>Letter:</label>
                <input class="normal-input" type="text" id="single-letter" maxlength="1" pattern="[A-Z]" hidden>

                <label class="normal-label-down">Name:</label>
                <input class="normal-input" type="text" id="output" readonly>
            </div>
            <span>
                <input type="submit" value="Generate Name" class="normal-btn" id="generate-name">
                <input type="button" value="Copy Name" class="normal-btn" id="copy-name">
            </span>
        """
    
    def get_js(self):
        return """
            const decreaseBtn = document.getElementById('decrease-btn');
            const increaseBtn = document.getElementById('increase-btn');
            const nameLengthInput = document.getElementById('name-length');
            const firstLetterInput = document.getElementById('first-letter');
            const fromLabel = document.getElementById('from-label');
            const fromLetterInput = document.getElementById('from-letter');
            const toLabel = document.getElementById('to-label');
            const toLetterInput = document.getElementById('to-letter');
            const singleLabel = document.getElementById('single-label');
            const singleLetterInput = document.getElementById('single-letter');
            const nameOutput = document.getElementById('output');
            const generateButton = document.getElementById('generate-name');
            const copyButton = document.getElementById('copy-name');

            const minLength = 3;
            const maxLength = 8;
            
            decreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let nameLength = parseInt(nameLengthInput.value, 10);
                if (!isNaN(nameLength)) {
                    nameLengthInput.value = Math.max(minLength, nameLength - 1);
                }
            });

            increaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let nameLength = parseInt(nameLengthInput.value, 10);
                if (!isNaN(nameLength)) {
                    nameLengthInput.value = Math.min(nameLength + 1, maxLength);
                }
            });

            fromLetterInput.addEventListener('input', (e) => {
                const value = e.target.value.toUpperCase();
                fromLetterInput.value = value;
            });

            toLetterInput.addEventListener('input', (e) => {
                const value = e.target.value.toUpperCase();
                toLetterInput.value = value;
            });

            singleLetterInput.addEventListener('input', (e) => {
                const value = e.target.value.toUpperCase();
                singleLetterInput.value = value;
            });

            firstLetterInput.addEventListener('change', (e) => {
                const value = e.target.value;
                if (value === 'from-to') {
                    fromLabel.removeAttribute('hidden');
                    fromLetterInput.removeAttribute('hidden');
                    fromLetterInput.setAttribute('required', true);

                    toLabel.removeAttribute('hidden');
                    toLetterInput.removeAttribute('hidden');
                    toLetterInput.setAttribute('required', true);

                    singleLabel.setAttribute('hidden', true);
                    singleLetterInput.setAttribute('hidden', true);
                    singleLabel.removeAttribute('required');
                } else if (value === 'single') {
                    fromLabel.setAttribute('hidden', true);
                    fromLetterInput.setAttribute('hidden', true);
                    fromLetterInput.removeAttribute('required');

                    toLabel.setAttribute('hidden', true);
                    toLetterInput.setAttribute('hidden', true);
                    toLetterInput.removeAttribute('required');

                    singleLabel.removeAttribute('hidden');
                    singleLetterInput.removeAttribute('hidden');
                    singleLetterInput.setAttribute('required', true);
                }
            });

            nameLengthInput.addEventListener('change', () => {
                if (nameLengthInput.value < minLength) {
                    nameLengthInput.value = minLength;
                }
                else if (nameLengthInput.value > maxLength) {
                    nameLengthInput.value = maxLength;
                }
            });

            generateButton.addEventListener('click', () => {
                try {
                    let randomName = '';
                    let attempts = 0;
                    const maxAttempts = 1000000;

                    if (firstLetterInput.value == 'single') {  
                        if (!isAlphabet(singleLetterInput.value)) {
                            alert ('Please type the single letter filter for the first letter first!');
                            return;
                        } 
                        do {
                            attempts += 1;
                            if (attempts > maxAttempts) {
                                alert ('Sorry, the tool took too long to generate random name. Please try again');
                                return;
                            }

                            randomName = exports.uniqueNamesGenerator ({
                                dictionaries: [exports.names],
                                style: 'capital'
                            });
                        } while (randomName.charAt(0) != singleLetterInput.value
                                || randomName.length != nameLengthInput.value);
                    }

                    else if (firstLetterInput.value == 'from-to') {
                        if (!isAlphabet(fromLetterInput.value) || !isAlphabet(toLetterInput.value)) {
                            alert ('Please type the range from-to letter for the first letter first!');
                            return;
                        }
                        do {
                            attempts += 1;
                            if (attempts > maxAttempts) {
                                alert ('Sorry, the tool took too long to generate random name. Please try again');
                                return;
                            }

                            randomName = exports.uniqueNamesGenerator ({
                                dictionaries: [exports.names],
                                style: 'capital'
                            });
                        } while (randomName.charAt(0) <= fromLetterInput.value 
                                || randomName.charAt(0) >= toLetterInput.value
                                || randomName.length != nameLengthInput.value);
                    }
                    console.log ('Attempts:', attempts);
                    nameOutput.value = randomName;
                } catch (err) {
                    console.error ('Failed to generate random name', err);
                    alert ('Failed to generate random name');
                }
                
            });

            copyButton.addEventListener('click', async () => {
                if (!nameOutput || nameOutput.value === '') {
                    alert ('Please generate name first!');
                    return;
                }
                try {
                    await navigator.clipboard.writeText(nameOutput.value);
                    alert ('Name copied to the clipboard successfully!');
                } catch (err) {
                    console.error ('Failed to copy name to the clipboard', err);
                    alert ('Failed to copy name to the clipboard');
                }
            });

            function isAlphabet(str) {
                return /^[a-zA-Z]+$/.test(str);
            }
        """
    
    def get_package(self):
        return "https://cdn.jsdelivr.net/npm/@joaomoreno/unique-names-generator@5.2.0/dist/index.min.js"