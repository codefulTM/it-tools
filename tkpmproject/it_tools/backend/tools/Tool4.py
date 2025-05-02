
from backend.classes.ToolComponent import ToolComponent

class Tool4(ToolComponent):
    def get_info(self):
        return {
            'id': 4,
            'name': 'Integer Base Converter',
            'description': 'A converter for integer base',
            'category': 'Converter',
            'is_premium': True,
            'is_enabled': True
        }

    def get_html(self):
        return """<h2 style="border-bottom:1px solid #444;padding-bottom:10px;">Integer base converter</h2>
<p style="color:#aaa;">Convert a number between different bases (decimal, hexadecimal, binary, octal, base64, ...)</p>

<div style="margin:20px 0;">
    <label>Input number<br>
        <input id="inputNumber" type="text" value="42"
            style="width:100%;padding:8px;background:#222;border:1px solid #555;color:white;">
    </label>
</div>

<hr style="border-color:#333;">

<div style="margin-top:20px;">
    <div>Binary (2)<br>
        <input id="outBin" readonly style="width:100%;padding:8px;background:#222;border:1px solid #555;color:white;">
    </div><br>

    <div>Octal (8)<br>
        <input id="outOct" readonly style="width:100%;padding:8px;background:#222;border:1px solid #555;color:white;">
    </div><br>

    <div>Decimal (10)<br>
        <input id="outDec" readonly style="width:100%;padding:8px;background:#222;border:1px solid #555;color:white;">
    </div><br>

    <div>Hexadecimal (16)<br>
        <input id="outHex" readonly style="width:100%;padding:8px;background:#222;border:1px solid #555;color:white;">
    </div><br>

    <div>Base64 (64)<br>
        <input id="outB64" readonly style="width:100%;padding:8px;background:#222;border:1px solid #555;color:white;">
    </div>
</div>"""

    def get_js(self):
        return """const inputNumber = document.getElementById("inputNumber");

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

convert();"""
        