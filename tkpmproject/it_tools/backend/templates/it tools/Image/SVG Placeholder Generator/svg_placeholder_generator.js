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