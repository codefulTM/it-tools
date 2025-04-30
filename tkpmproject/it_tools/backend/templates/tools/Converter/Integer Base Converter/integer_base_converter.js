const inputNumber = document.getElementById("inputNumber");

const outBin = document.getElementById("outBin");
const outOct = document.getElementById("outOct");
const outDec = document.getElementById("outDec");
const outHex = document.getElementById("outHex");
const outB64 = document.getElementById("outB64");

const base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

function toBase64(num) {
    const base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    if (num === 0) return "A";

    let result = "";
    while (num > 0) {
        let remainder = num % 64;
        result = base64Chars[remainder] + result;
        num = Math.floor(num / 64);
    }
    return result;
}

function convert() {
    const numStr = inputNumber.value.trim();
    let number;

    try {
        number = parseInt(numStr);
        if (isNaN(number)) throw new Error("Invalid");
    } catch {
        outBin.value = outOct.value = outDec.value = outHex.value = outB64.value = outCustom.value = "Invalid";
        return;
    }

    outBin.value = number.toString(2);
    outOct.value = number.toString(8);
    outDec.value = number.toString(10);
    outHex.value = number.toString(16);

    // Base64
    outB64.value = toBase64(number);
}

inputNumber.addEventListener("input", convert);

convert();