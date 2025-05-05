const fileInput = document.getElementById("file");
const textInput = document.getElementById("text");
const formattedJSON = document.getElementById("formatted-text");
const formatJSON = document.getElementById("format-json");
const downloadJSON = document.getElementById("download-json");

fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        if (!file) {
            showMessage("No file selected. Please choose a file.", "error");
            return;
        }
        const reader = new FileReader();
        reader.onload = function (readEvent) {
            let fileContent = readEvent.target.result;
            console.log(fileContent); 

            textInput.value = fileContent;
        };
        reader.onerror = function () {
            showMessage("Error reading the file. Please try again.", "error");
        };
        reader.readAsText(file);
    }
});

textInput.addEventListener("change", () => {
    if (textInput.value.trim() !== '') {
        fileInput.value = '';
    }
});

formatJSON.addEventListener("click", () => {
    if (!textInput || textInput.value == '') {
        alert ("Please input the JSON content or choose the JSON file first!");
        return;
    }

    try {
        const parsed = JSON.parse(textInput.value);
        const formatted = JSON.stringify(parsed, null, 4);
        formattedJSON.value = formatted;
    } catch (err) {
        console.error ("Failed to format JSON content");
        alert ("Failed to format JSON content");
    }
});

downloadJSON.addEventListener("click", () => {
    if (!formattedJSON || formattedJSON.value == '') {
        alert ("Please format the JSON content first!");
        return;
    }

    try {
        const blob = new Blob ([formattedJSON.value], { type: "application/json" });
        const url = URL.createObjectURL(blob);

        const a = document.createElement('a');
        a.href = url;
        a.download = "formatted.json"; // File name
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);

        URL.revokeObjectURL(url);
    } catch (err) {
        console.error ("Failed to download formatted JSON file", err);
        alert ("Failed to download formatted JSON file");
    }
});