function calcPercentOf() {
    let x = parseFloat(document.getElementById("x1").value);
    let y = parseFloat(document.getElementById("y1").value);
    if (!isNaN(x) && !isNaN(y)) {
        document.getElementById("result1").value = ((x / 100) * y).toFixed(2);
    }
}

function calcWhatPercent() {
    let x = parseFloat(document.getElementById("x2").value);
    let y = parseFloat(document.getElementById("y2").value);
    if (!isNaN(x) && !isNaN(y) && y !== 0) {
        document.getElementById("result2").value = ((x / y) * 100).toFixed(2) + "%";
    }
}

function calcIncreaseDecrease() {
    let from = parseFloat(document.getElementById("from").value);
    let to = parseFloat(document.getElementById("to").value);
    if (!isNaN(from) && !isNaN(to) && from !== 0) {
        let change = ((to - from) / from) * 100;
        document.getElementById("result3").value = change.toFixed(2) + "%";
    }
}

function copyResult(id) {
    let copyText = document.getElementById(id);
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
    document.execCommand("copy");
    alert("Copied: " + copyText.value);
}