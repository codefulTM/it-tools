from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool17(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(17)

        if (info != None):
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled
            
            return {
                'id': 17, 
                'name': self.name,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }
        
        else:
            print("Error: Cannot retrieve the info for tool id 17")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>

            <p class="tool-des">{self.description} </p>

            <div class="tool-body qr-code-generator-container">
                <label class="normal-label-down">Encryption method:</label>
                <select name="encryption-method" class="dropdown" id="encryption">
                    <option value="">No password</option>
                    <option value="WPA" selected>WPA/WPA2</option>
                    <option value="WERP">WEP</option>
                    <option value="EAP">WPA2-EAP</option>
                </select>

                <label class="normal-label">SSID:</label>
                <input class="normal-input" type="text" id="ssid" required>
                
                <label class="normal-label" id="label-password">Password:</label>
                <input class="normal-input" type="password" id="input-password" required>
            
                <label class="normal-label-down">Foreground color:</label>
                <div class="color-picker-wrapper">
                    <input type="color" id="input-foreground" value="#000000">
                    <input type="text" id="foreground-hex" class="hex-value" readonly>
                </div>

                <label class="normal-label-down">Background color:</label>
                <div class="color-picker-wrapper">
                    <input type="color" id="input-background" value="#ffffff">
                    <input type="text" id="background-hex" class="hex-value" readonly>
                </div>

                <label class="normal-label">Hidden SSID</label>
                <input type="checkbox" name="hidden-ssid" checked="checked" id="ssid-checkbox">
                <img id="qr-code">
            </div>  

            <span>
                <input type="submit" value="Generate QR Code" class="normal-btn" id="generate-qr-code">
                <input type="button" value="Copy QR Code" class="normal-btn" id="copy-qr-code">
            </span>
        """
    
    def get_js(self):
        return """
            const foregroundColorInput = document.getElementById('input-foreground');
            const backgroundColorInput = document.getElementById('input-background');
            const foregroundHex = document.getElementById('foreground-hex');
            const backgroundHex = document.getElementById('background-hex');
            const encryptionValue = document.getElementById('encryption');
            const passwordLabel = document.getElementById('label-password');
            const passwordInput = document.getElementById('input-password');
            const ssidCheckbox = document.getElementById('ssid-checkbox');
            const ssidInput = document.getElementById('ssid');
            const generateButton = document.getElementById('generate-qr-code');
            const copyButton = document.getElementById('copy-qr-code');
            const qrCodeOutput = document.getElementById('qr-code');

            generateButton.addEventListener('click', async () => {
                try {
                    var wifiString = ""
                    if (encryption.value == "")
                        wifiString = `WIFI:T:;S:${ssidInput.value};H:${ssidCheckbox.checked};;`;
                    else
                        wifiString = `WIFI:T:${encryptionValue.value};S:${ssidInput.value};P:${passwordInput.value};H:${ssidCheckbox.checked};;`;

                    const options = {
                        errorCorrectionLevel: 'Q',
                        color: {
                            dark: foregroundColorInput.value,
                            light: backgroundColorInput.value
                        },
                        width: 256
                    };

                    const dataUrl = await QRCode.toDataURL(wifiString, options);

                    console.log('Generated WiFi QR Code Data URL:');
                    console.log(dataUrl);

                    qrCodeOutput.src = dataUrl;
                } catch (err) {
                    console.error('Failed to generate QR Code', err);
                    alert('Failed to copy QR Code');
                }
            });

            copyButton.addEventListener('click', async () => {
                if (!qrCodeOutput || !qrCodeOutput.src) {
                    alert('Please generate a QR code first!');
                    return;
                }

                try {
                    const response = await fetch(qrCodeOutput.src);
                    const blob = await response.blob();

                    const clipboardItem = new ClipboardItem({ [blob.type]: blob });

                    await navigator.clipboard.write([clipboardItem]);

                    alert('QR Code copied to clipboard successfully!');
                } catch (err) {
                    console.error('Failed to copy QR Code:', err);
                    alert('Failed to copy QR Code');
                }
            });

            function updateForegroundColor(hex) {
                foregroundHex.value = hex;
            }

            foregroundColorInput.addEventListener('input', (e) => {
                updateForegroundColor(e.target.value);
            });

            updateForegroundColor(foregroundColorInput.value);

            function updateBackgroundColor(hex) {
                backgroundHex.value = hex;
            }

            backgroundColorInput.addEventListener('input', (e) => {
                updateBackgroundColor(e.target.value);
            });

            updateBackgroundColor(backgroundColorInput.value);

            encryptionValue.addEventListener('change', (e) => {
                changeEncryption();
            });
            
            function changeEncryption() {
                if (encryptionValue.value == "") {
                    passwordInput.value = "";
                    passwordInput.disabled = true;
                    passwordInput.removeAttribute('required');
                    passwordInput.setAttribute('hidden', true);
                    passwordLabel.setAttribute('hidden', true);
                } else {
                    passwordInput.disabled = false;
                    passwordInput.setAttribute('required', true);
                    passwordInput.removeAttribute('hidden');
                    passwordLabel.removeAttribute('hidden');
                }
            }
        """
    
    def get_package(self):
        return "https://cdn.jsdelivr.net/npm/qrcode@1.5.1/build/qrcode.min.js"