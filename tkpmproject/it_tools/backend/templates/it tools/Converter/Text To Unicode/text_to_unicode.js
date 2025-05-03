const textInput = document.getElementById('textInput');
const unicodeOutput = document.getElementById('unicodeOutput');
const unicodeInput = document.getElementById('unicodeInput');
const textOutput = document.getElementById('textOutput');

textInput.addEventListener('input', () => {
    const text = textInput.value;
    let result = '';
    for (let char of text) {
        result += `&#${char.charCodeAt(0)};`;
    }
    unicodeOutput.value = result;
});

unicodeInput.addEventListener('input', () => {
    const unicodeStr = unicodeInput.value;
    try {
        // decode HTML entities
        const parser = new DOMParser();
        const decoded = parser.parseFromString(unicodeStr, 'text/html').documentElement.textContent;
        textOutput.value = decoded;
    } catch (e) {
        textOutput.value = 'Invalid Unicode input';
    }
});

function copyToClipboard(id) {
    const el = document.getElementById(id);
    el.select();
    document.execCommand("copy");
}