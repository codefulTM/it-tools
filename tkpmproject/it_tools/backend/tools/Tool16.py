import qrcode as qr
import qrcode.image.svg
from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from io import BytesIO
import json

class Tool16(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(16)

        if (info != None):  
            self.name = info.name
            self.description = info.description
            self.category = info.category.name
            self.is_premium = info.is_premium
            self.is_enabled = info.is_enabled

            return {
                'id': 16,
                'name': self.name,
                'description': self.description,
                'category': self.category,
                'is_premium': self.is_premium,
                'is_enabled': self.is_enabled
            }

        else:
            print("Error: Cannot retrieve the info for tool id 16")
            return None

    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>
            <p class="tool-des">{self.description}</p>

            <form action="/tools/16/" method="post">
                <div class="tool-body qr-code-generator-container">
                    <label class="normal-label">Text:</label>
                    <textarea class="normal-input" type="text" id="text" required></textarea>
                
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

                    <label class="normal-label-down">Error resistance:</label>
                    <select name="error-resistance" class="dropdown" id="error-resistance">
                        <option value="L">low (7%)</option>
                        <option value="M">medium (15%)</option>
                        <option value="Q">quartile (25%)</option>
                        <option value="H">high (30%)</option>
                    </select>
                    <img id="qr-code">
                </div>  

                <span>
                    <input type="button" value="Generate QR Code" class="normal-btn" id="generate-qr-code">
                    <input type="button" value="Copy QR Code" class="normal-btn" id="copy-qr-code">
                </span>
            </form>    
        """
    
    def get_js(self):
        return """
            const foregroundColorInput = document.getElementById('input-foreground');
            const backgroundColorInput = document.getElementById('input-background');
            const foregroundHex = document.getElementById('foreground-hex');
            const backgroundHex = document.getElementById('background-hex');
            const textInput = document.getElementById('text');
            const errorResistance = document.getElementById('error-resistance');
            const generateButton = document.getElementById('generate-qr-code');
            const copyButton = document.getElementById('copy-qr-code');
            const qrCodeOutput = document.getElementById('qr-code');

            generateButton.addEventListener('click', async () => {
                try {
                    const options = {
                        errorCorrectionLevel: errorResistance.value,
                        color: {
                            dark: foregroundColorInput.value,
                            light: backgroundColorInput.value
                        },
                        width: 256
                    };

                    const dataUrl = await QRCode.toDataURL(textInput.value, options);

                    console.log('Generated QR Code Data URL:');
                    console.log(dataUrl);

                    qrCodeOutput.src = dataUrl;
                } catch (err) {
                    console.error('Failed to generate QR Code', err);
                }
            });

            copyButton.addEventListener('click', async () => {
                const qrImage = document.getElementById('qr-code');

                if (!qrImage || !qrImage.src) {
                    alert('Please generate a QR code first!');
                    return;
                }

                try {
                    const response = await fetch(qrImage.src);
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
        """
    
    def get_package(self):
        return "https://cdn.jsdelivr.net/npm/qrcode@1.5.1/build/qrcode.min.js"