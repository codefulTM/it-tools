const foregroundColorInput = document.getElementById('input-foreground');
const backgroundColorInput = document.getElementById('input-background');

const foregroundHex = document.getElementById('foreground-hex');
const backgroundHex = document.getElementById('background-hex');

const encryptionValue = document.getElementById('encryption');

const passwordLabel = document.getElementById('label-password');
const passwordInput = document.getElementById('input-password');

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
    if (encryptionValue.value == "no") {
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