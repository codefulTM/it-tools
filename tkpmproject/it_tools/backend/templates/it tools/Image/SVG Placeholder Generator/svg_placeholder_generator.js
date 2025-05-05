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