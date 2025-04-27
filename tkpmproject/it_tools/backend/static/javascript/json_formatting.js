const fileInput = document.getElementById("file");
const textInput = document.getElementById("text");

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        textInput.value = '';
        fileInput.setAttribute('required', true);
        textInput.removeAttribute('required');
    }
});

textInput.addEventListener('input', () => {
    if (textInput.value.trim() !== '') {
        fileInput.value = '';
        textInput.setAttribute('required', true);
        fileInput.removeAttribute('required');
    }
})