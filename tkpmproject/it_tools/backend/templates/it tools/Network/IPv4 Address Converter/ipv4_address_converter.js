const ipInput = document.getElementById('ip');
const outDec = document.getElementById('outDec');
const outHex = document.getElementById('outHex');
const outBin = document.getElementById('outBin');
const outIPv6 = document.getElementById('outIPv6');
const outIPv6short = document.getElementById('outIPv6short');

function convert() {
    const ip = ipInput.value.trim();
    const parts = ip.split('.');
    if (parts.length !== 4 || parts.some(p => isNaN(p) || p < 0 || p > 255)) {
        [outDec, outHex, outBin, outIPv6, outIPv6short].forEach(el => el.value = '');
        return;
    }
    const oct = parts.map(p => parseInt(p, 10));
    // Decimal
    const dec = oct[0] * 16777216 + oct[1] * 65536 + oct[2] * 256 + oct[3];
    outDec.value = dec;

    // Hexadecimal (8 hex digits)
    const hex = oct.map(b => b.toString(16).padStart(2, '0')).join('').toUpperCase();
    outHex.value = hex;

    // Binary (32 bits)
    const bin = oct.map(b => b.toString(2).padStart(8, '0')).join('');
    outBin.value = bin;

    // IPv6 full
    const h6 = oct[0].toString(16).padStart(2, '0') + oct[1].toString(16).padStart(2, '0');
    const h7 = oct[2].toString(16).padStart(2, '0') + oct[3].toString(16).padStart(2, '0');
    const full6 = ['0000', '0000', '0000', '0000', '0000', 'ffff', h6, h7].join(':');
    outIPv6.value = full6;

    // IPv6 short
    outIPv6short.value = full6.replace(/^0000(:0000){4}:/, '::');
}

function copyValue(id) {
    const el = document.getElementById(id);
    el.select();
    document.execCommand('copy');
    alert("Copied!")
}

ipInput.addEventListener('input', convert);
window.addEventListener('load', convert);