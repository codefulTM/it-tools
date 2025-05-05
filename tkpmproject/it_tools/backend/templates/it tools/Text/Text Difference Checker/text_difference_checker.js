const fileInput1 = document.getElementById('file1');
const fileInput2 = document.getElementById('file2');
const textArea1 = document.getElementById('text1');
const textArea2 = document.getElementById('text2');
const resultDiv = document.getElementById('result');
const checkDiffButton = document.getElementById('check-difference');

fileInput1.addEventListener('change', readFile, false);

fileInput2.addEventListener('change', readFile, false);

textArea1.addEventListener('input', () => {
    if (textArea1.value.trim() !== '') {
        fileInput1.value = ''; 
    }
});

textArea2.addEventListener('input', () => {
    if (textArea2.value.trim() !== '') {
        fileInput2.value = '';
    }
});

checkDiffButton.addEventListener('click', () => {
    const text1 = textArea1.value;
    const text2 = textArea2.value;

    if (text1 == '' || text2 == '') {
        alert ('Please paste your text or choose a file first!');
        return;
    }

    const diff = diffWordsWithSpace(text1, text2);
    resultDiv.innerHTML = '';

    diff.forEach((part) => {
        let safeText = part.value
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/\\n/g, '<br>');

        const span = document.createElement('span');
        span.style.fontSize = '24px';
        span.innerHTML = safeText;

        if (part.added) {
            span.style.backgroundColor = 'lightgreen';
        } else if (part.removed) {
            span.style.backgroundColor = 'lightcoral';
        }

        resultDiv.appendChild(span);
    });
});

function readFile(event) {
    const file = event.target.files[0];
    if (!file) {
        showMessage("No file selected. Please choose a file.", "error");
        return;
    }
    const reader = new FileReader();
    reader.onload = function (readEvent) {
        let fileContent = readEvent.target.result;
        console.log(fileContent); 

        if (event.target.id === 'file1')
            textArea1.value = fileContent;
        else if (event.target.id === 'file2')
            textArea2.value = fileContent;
    };
    reader.onerror = function () {
        showMessage("Error reading the file. Please try again.", "error");
    };
    reader.readAsText(file);
}

function diffWordsWithSpace(text1, text2) {
    const words1 = text1.split(/(\s+)/); // include spaces in split
    const words2 = text2.split(/(\s+)/);

    let i = 0, j = 0;
    const diff = [];

    while (i < words1.length && j < words2.length) {
        if (words1[i] === words2[j]) {
            diff.push({ value: words1[i] });
            i++;
            j++;
        } else {
            diff.push({ value: words1[i], removed: true });
            diff.push({ value: words2[j], added: true });
            i++;
            j++;
        }
    }

    while (i < words1.length) {
        diff.push({ value: words1[i], removed: true });
        i++;
    }

    while (j < words2.length) {
        diff.push({ value: words2[j], added: true });
        j++;
    }

    return diff;
}
