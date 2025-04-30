from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool19(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(19)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 18, 
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 19")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>
            <p class="tool-des">{self.description}</p>

            <div class="tool-body prime-generator-container">
                <label class="normal-label">From:</label>
                <div class="number-input">
                    <button class="btn decrement" id="prime-from-decrease-btn">−</button>
                    <input type="number" id="prime-from" value="2" required>
                    <button class="btn increment" id="prime-from-increase-btn">+</button>
                </div>

                <label class="normal-label">To:</label>
                <div class="number-input">
                    <button class="btn decrement" id="prime-to-decrease-btn">−</button>
                    <input type="number" id="prime-to" value="10000" required>
                    <button class="btn increment" id="prime-to-increase-btn">+</button>
                </div>

                <label class="normal-label">Prime:</label>
                <input class="normal-input" type="number" id="prime-output" readonly>
            </div>
            <span>
                <input type="submit" value="Generate Prime" class="normal-btn" id="generate-prime">
                <input type="button" value="Copy Prime" class="normal-btn" id="copy-prime">
            </span>

        """
    
    def get_js(self):
        return """
            const primeFromDecreaseBtn = document.getElementById('prime-from-decrease-btn');
            const primeFromIncreaseBtn = document.getElementById('prime-from-increase-btn');
            const primeToDecreaseBtn = document.getElementById('prime-to-decrease-btn');
            const primtToIncreaseBtn = document.getElementById('prime-to-increase-btn');
            const primeFromInput = document.getElementById('prime-from');
            const primeToInput = document.getElementById('prime-to');
            const primeOutput = document.getElementById('prime-output');
            const generatePrime = document.getElementById('generate-prime');
            const copyPrime = document.getElementById('copy-prime');

            primeFromDecreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let primeFrom = parseInt(primeFromInput.value, 10);
                let primeTo = parseInt(primeToInput.value, 10);
                if (!isNaN(primeFrom) && !isNaN(primeTo)) {
                    primeFromInput.value = Math.max(2, primeFrom - 1);
                }
            });

            primeFromIncreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let primeFrom = parseInt(primeFromInput.value, 10);
                let primeTo = parseInt(primeToInput.value, 10);
                if (!isNaN(primeFrom) && !isNaN(primeTo)) {
                    primeFromInput.value = Math.min(primeFrom + 1, primeTo);
                }
            });

            primeToDecreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let primeFrom = parseInt(primeFromInput.value, 10);
                let primeTo = parseInt(primeToInput.value, 10);
                if (!isNaN(primeFrom) && !isNaN(primeTo)) {
                    primeToInput.value = Math.max(primeFrom, primeTo - 1);
                }
            });

            primtToIncreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let primeFrom = parseInt(primeFromInput.value, 10);
                let primeTo = parseInt(primeToInput.value, 10);
                if (!isNaN(primeFrom) && !isNaN(primeTo)) {
                    primeToInput.value = primeTo + 1;
                }
            });

            primeFromInput.addEventListener('change', (e) => {
                let primeFrom = parseInt(primeFromInput.value, 10);
                let primeTo = parseInt(primeToInput.value, 10);
                if (!isNaN(primeFrom) && !isNaN(primeTo)) {
                    primeFrom = Math.max(primeFrom, 2);
                    primeFromInput.value = primeFrom;
                    primeTo = Math.max(primeFrom, primeTo);
                    primeToInput.value = primeTo;
                }
            });

            primeToInput.addEventListener('change', (e) => {
                let primeFrom = parseInt(primeFromInput.value, 10);
                let primeTo = parseInt(primeToInput.value, 10);
                if (!isNaN(primeFrom) && !isNaN(primeTo)) {
                    primeTo = Math.max(2, primeTo);
                    primeToInput.value = primeTo;
                    primeFrom = Math.min(primeTo, primeFrom);
                    primeFromInput.value = primeFrom;
                }
            });

            generatePrime.addEventListener('click', () => {
                try {         
                    primeOutput.value = generateRandomPrime(primeFromInput.value, primeToInput.value);
                } catch (err) {
                    console.error('Failed to generate random prime', err);
                    alert('Failed to generate random prime');
                }
            });

            copyPrime.addEventListener('click', async () => {
                if (!primeOutput || primeOutput.value == '') {
                    alert('Please generate prime first!');
                    return;
                }

                try {
                    await navigator.clipboard.writeText(primeOutput.value);
                    alert('Prime copied to the clipboard successfully');
                } catch (err) {
                    console.error('Failed to copy prime', err);
                    alert('Failed to copy prime');
                }
            });

            function generateRandomPrime(min, max) {
                while (true) {
                    const num = getRandomInt(min, max);
                    if (millerRabin(num)) return num;
                }
            }
            
            function getRandomInt(min, max) {
                min = Math.ceil(min);
                max = Math.floor(max);
                return Math.floor(Math.random() * (max - min + 1)) + min;
            }

            function power(base, exp, mod) {
                let res = 1;
                base %= mod;
                while (exp > 0) {
                    if (exp % 2 === 1) res = (res * base) % mod;
                    base = (base * base) % mod;
                    exp = Math.floor(exp / 2);
                }
                return res;
            }

            function millerRabin(n, k = 5) {
                if (n <= 1 || n === 4) return false;
                if (n <= 3) return true;

                let d = n - 1;
                while (d % 2 === 0) d /= 2;

                for (let i = 0; i < k; i++) {
                    let a = 2 + Math.floor(Math.random() * (n - 4));
                    let x = power(a, d, n);

                    if (x === 1 || x === n - 1) continue;

                    while (d !== n - 1) {
                    x = (x * x) % n;
                    d *= 2;
                    if (x === 1) return false;
                    if (x === n - 1) break;
                    }
                    if (x !== n - 1) return false;
                }
                return true;
            }
        """
    
    def get_package(self):
        return ""