from backend.classes.ToolComponent import ToolComponent
from data_service.services.tool_services import get_tool_by_id

class Tool18(ToolComponent):
    def get_info(self):
        info = get_tool_by_id(18)

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
            print("Error: Cannot retrieve the info for tool id 18")
            return None
        
    def get_html(self):
        return f"""
            <h2 class="tool-name">{self.name}</h2>

            <p class="tool-des">{self.description}</p>

            <div class="svg-container tool-body">
                <label class="normal-label-down">Width (in px):</label>
                <div class="number-input">
                    <button class="btn decrement" id="width-decrease-btn">−</button>
                    <input type="number" id="svg-width" value="100" required>
                    <button class="btn increment" id="width-increase-btn">+</button>
                </div>

                <label class="normal-label-down">Text color:</label>
                <div class="color-picker-wrapper">
                    <input type="color" id="input-foreground" value="#000000">
                    <input type="text" id="foreground-hex" class="hex-value">
                </div>

                <label class="normal-label-down">Height (in px):</label>
                <div class="number-input">
                    <button class="btn decrement" id="height-decrease-btn">−</button>
                    <input type="number" id="svg-height" value="100" required>
                    <button class="btn increment" id="height-increase-btn">+</button>
                </div>
            
                <label class="normal-label-down">Background:</label>
                <div class="color-picker-wrapper">
                    <input type="color" id="input-background" value="#ffffff">
                    <input type="text" id="background-hex" class="hex-value" readonly>
                </div>

                <label class="normal-label-down">Font size:</label>
                <div class="number-input">
                    <button class="btn decrement" id="size-decrease-btn">−</button>
                    <input type="number" id="font-size" value="20" required>
                    <button class="btn increment" id="size-increase-btn">+</button>
                </div>

                <label class="normal-label-down">Custom text</label>
                <input class="normal-input" type="text" placeholder="Default" id="text" required>
            </div>

            <input type="submit" value="Generate SVG Placeholder" class="normal-btn" id="generate-svg">
            <input type="button" value="Download SVG" class="normal-btn" id="download-svg">
            <input type="button" value="Copy SVG HTML" class="normal-btn" id="copy-svg-html">
            <input type="button" value="Copy SVG base64" class="normal-btn" id="copy-svg-base64">

            <div class="svg-output-container tool-body">
                <label class="normal-label-down">SVG HTML element</label>
                <textarea class="normal-input" rows="10" type="text" id="svg-html-output" readonly></textarea>    
                <label class="normal-label-down">SVG in Base64</label>
                <textarea class="normal-input" rows="10" type="text" id="svg-base64-output" readonly></textarea>
            </div>
        """
    
    def get_js(self):
        return """
            const foregroundColorInput = document.getElementById('input-foreground');
            const backgroundColorInput = document.getElementById('input-background');
            const foregroundHex = document.getElementById('foreground-hex');
            const backgroundHex = document.getElementById('background-hex');

            const widthDecreaseBtn = document.getElementById('width-decrease-btn');
            const widthIncreaseBtn = document.getElementById('width-increase-btn');
            const svgWidthInput = document.getElementById('svg-width');

            const heightDecreaseBtn = document.getElementById('height-decrease-btn');
            const heightIncreaseBtn = document.getElementById('height-increase-btn');
            const svgHeightInput = document.getElementById('svg-height');

            const sizeDecreaseBtn = document.getElementById('size-decrease-btn');
            const sizeIncreaseBtn = document.getElementById('size-increase-btn');
            const fontSizeInput = document.getElementById('font-size');

            const textInput = document.getElementById('text');
            const svgHTMLOutput = document.getElementById('svg-html-output');
            const svgBase64Output = document.getElementById('svg-base64-output');

            const generateSVG = document.getElementById('generate-svg');
            const downloadSVG = document.getElementById('download-svg');
            const copySVGHTML = document.getElementById('copy-svg-html');
            const copySVGBase64 = document.getElementById('copy-svg-base64');

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

            widthDecreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let currentValue = parseInt(svgWidthInput.value, 10);
                if (!isNaN(currentValue)) {
                    svgWidthInput.value = Math.max(0, currentValue - 1);
                }
            });

            widthIncreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let currentValue = parseInt(svgWidthInput.value, 10);
                if (!isNaN(currentValue)) {
                    svgWidthInput.value = currentValue + 1;
                }
            });

            heightDecreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let currentValue = parseInt(svgHeightInput.value, 10);
                if (!isNaN(currentValue)) {
                    svgHeightInput.value = Math.max(0, currentValue - 1);
                }
            });

            heightIncreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let currentValue = parseInt(svgHeightInput.value, 10);
                if (!isNaN(currentValue)) {
                    svgHeightInput.value = currentValue + 1;
                }
            });

            sizeDecreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let currentValue = parseInt(fontSizeInput.value, 10);
                if (!isNaN(currentValue)) {
                    fontSizeInput.value = Math.max(6, currentValue - 1);
                }
            });

            sizeIncreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                let currentValue = parseInt(fontSizeInput.value, 10);
                if (!isNaN(currentValue)) {
                    fontSizeInput.value = currentValue + 1;
                }
            });

            generateSVG.addEventListener('click', () => {
                try {
                    const svgHTML = `
<svg xmlns="http://www.w3.org/2000/svg" width="${svgWidthInput.value}" height="${svgHeightInput.value}">
    <rect width="100%" height="100%" fill="${backgroundColorInput.value}" />
    <text x="50%" y="50%" 
            fill="${foregroundColorInput.value}" 
            font-size="${fontSizeInput.value}" 
            dominant-baseline="middle" 
            text-anchor="middle" 
            font-family="Arial, sans-serif">
        ${textInput.value == '' ? 'Default' : textInput.value}
    </text>
</svg>
                    `.trim();
                    svgHTMLOutput.value = svgHTML;

                    const svgBase64 = `data:image/svg+xml;base64,${btoa(unescape(encodeURIComponent(svgHTML)))}`;
                    svgBase64Output.value = svgBase64;
                } catch (err) {
                    console.error('Failed to generate SVG Placeholder', err);
                    alert('Failed to generate SVG Placeholder');
                }
            });

            downloadSVG.addEventListener('click', async () => {
                if (!svgHTMLOutput || svgHTMLOutput.value == ''){
                    alert('Please generate SVG Placeholder first!');
                    return;
                }

                try {
                    const blob = new Blob([svgHTMLOutput.value], { type: 'image/svg+xml'});
                    const url = URL.createObjectURL(blob);

                    const a = document.createElement('a');
                    a.href = url;
                    a.download = 'placeholder.svg';
                    document.body.appendChild(a);
                    a.click();

                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                } catch (err) {
                    console.error('Failed to download SVG file', err);
                    alert('Failed to download SVG file');
                }
            })

            copySVGHTML.addEventListener('click', async () => {
                if (!svgHTMLOutput || svgHTMLOutput.value == ''){
                    alert('Please generate SVG Placeholder first!');
                    return;
                }

                try {
                    await navigator.clipboard.writeText(svgHTMLOutput.value);
                    alert ('SVG HTML copied to the clipboard successfully!');
                } catch (err) {
                    console.error('Failed to copy SVG HTML to the clipboard', err);
                    alert('Failed to copy SVG HTML to the clipboard');
                }
            })

            copySVGBase64.addEventListener('click', async () => {
                if (!svgBase64Output || svgBase64Output.value == ''){
                    alert('Please generate SVG Placeholder first!');
                    return;
                }

                try {
                    await navigator.clipboard.writeText(svgBase64Output.value);
                    alert ('SVG Base64 copied to the clipboard successfully!');
                } catch (err) {
                    console.error('Failed to copy SVG Base64 to the clipboard', err);
                    alert('Failed to copy SVG Base64 to the clipboard');
                }
            })
        """
    
    def get_package(self):
        return "https://cdn.jsdelivr.net/npm/qrcode@1.5.1/build/qrcode.min.js"