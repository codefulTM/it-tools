const foregroundColorInput = document.getElementById('input-foreground');
const backgroundColorInput = document.getElementById('input-background');
const foregroundHex = document.getElementById('foreground-hex');
const backgroundHex = document.getElementById('background-hex');

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