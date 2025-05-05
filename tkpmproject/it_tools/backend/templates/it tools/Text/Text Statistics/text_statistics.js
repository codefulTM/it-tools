const fileInput = document.getElementById('file');
const textArea = document.getElementById('text');
const charsCount = document.getElementById('characters');
const wordsCount = document.getElementById('words');
const linesCount = document.getElementById('lines');
const sizeCount = document.getElementById('size');

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        if (!file) {
            showMessage("No file selected. Please choose a file.", "error");
            return;
        }
        const reader = new FileReader();
        reader.onload = function (readEvent) {
            let fileContent = readEvent.target.result;
            textArea.value = fileContent;
            sizeCount.value = file.size;
            updateStatistics();

            console.log(fileContent); 
        };
        reader.onerror = function () {
            showMessage("Error reading the file. Please try again.", "error");
        };
        reader.readAsText(file);
    }
});

textArea.addEventListener('change', () => {
    fileInput.value = '';
    updateStatistics();
});

function updateStatistics() {
    const text = textArea.value;

    if (text == '') {
        charsCount.value = 0;
        wordsCount.value = 0;
        linesCount.value = 0;
        sizeCount.value = 0;
        return;
    }

    charsCount.value = text.replace(/\s/g, '').length;
    wordsCount.value = text.match(/\S+/g).length;
    linesCount.value = text.split(/\\n/).length;
    if (fileInput.value == '')
        sizeCount.value = (new Blob([text])).size;
}