const foregroundColorInput = document.getElementById('input-foreground');
const backgroundColorInput = document.getElementById('input-background');
const foregroundHex = document.getElementById('foreground-hex');
const backgroundHex = document.getElementById('background-hex');
const encryptionValue = document.getElementById('encryption');
const passwordLabel = document.getElementById('label-password');
const passwordInput = document.getElementById('input-password');
const ssidCheckbox = document.getElementById('ssid-checkbox');
const ssidInput = document.getElementById('ssid');
const generateButton = document.getElementById('generate-qr-code');
const copyButton = document.getElementById('copy-qr-code');
const qrCodeOutput = document.getElementById('qr-code');

generateButton.addEventListener('click', async () => {
    try {
        const ssid = ssidInput.value.trim();
        const password = passwordInput.value;
        const encryption = encryptionValue.value;
        const hidden = ssidCheckbox.checked;

        let wifiString = 'WIFI:';
        if (encryption == '') wifiString += `T:${'nopass'};`;
        else wifiString += `T:${encryption}`;
        wifiString += `S:${ssid};`;
        if (encryption) wifiString += `P:${password};`;
        if (hidden) wifiString += `H:${hidden};`;

        wifiString += ';'; // end marker

        const dataUrl = generateQRCode(wifiString.toUpperCase(), 'Q', foregroundColorInput.value, backgroundColorInput.value);
        qrCodeOutput.src = dataUrl;
    } catch (err) {
        console.error('Failed to generate QR Code:', err);
        alert('Failed to generate QR Code');
    }
});

copyButton.addEventListener('click', async () => {
    if (!qrCodeOutput || !qrCodeOutput.src) {
        alert('Please generate a QR code first!');
        return;
    }

    try {
        const response = await fetch(qrCodeOutput.src);
        const blob = await response.blob();

        const clipboardItem = new ClipboardItem({ [blob.type]: blob });

        await navigator.clipboard.write([clipboardItem]);

        alert('QR Code copied to clipboard successfully!');
    } catch (err) {
        console.error('Failed to copy QR Code:', err);
        alert('Failed to copy QR Code');
    }
});

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
    if (encryptionValue.value == "") {
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

// Pure JavaScript QR Code generator for Version 1 (21x21)
// Supports alphanumeric encoding, Reed-Solomon ECC, canvas rendering (no external libraries)

const ALPHANUMERIC_CHARSET = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:';

const ECC_LEVELS = {
    L: { ecCodewordsPerBlock: 7, blocks: 1 },
    M: { ecCodewordsPerBlock: 10, blocks: 1 },
    Q: { ecCodewordsPerBlock: 13, blocks: 1 },
    H: { ecCodewordsPerBlock: 17, blocks: 1 },
};

const GF256 = (() => {
    const EXP = new Uint8Array(512);
    const LOG = new Uint8Array(256);
    let x = 1;
    for (let i = 0; i < 255; i++) {
        EXP[i] = x;
        LOG[x] = i;
        x <<= 1;
        if (x & 0x100) x ^= 0x11d;
    }
    for (let i = 255; i < 512; i++) EXP[i] = EXP[i - 255];
    return {
        add: (a, b) => a ^ b,
        mul: (a, b) => (a && b ? EXP[LOG[a] + LOG[b]] : 0),
        div: (a, b) => (a && b ? EXP[(LOG[a] + 255 - LOG[b]) % 255] : 0),
        EXP, LOG
    };
})();

function genPoly(ecLen) {
    let poly = [1];
    for (let i = 0; i < ecLen; i++) {
        let next = [1];
        for (let j = 0; j < poly.length; j++) next[j + 1] = GF256.mul(poly[j], GF256.EXP[i]);
        for (let j = 0; j < poly.length; j++) next[j] ^= GF256.mul(poly[j], 1);
        poly = next;
    }
    return poly;
}

function reedSolomonEncode(data, ecLen) {
    const result = new Uint8Array(ecLen);
    for (let i = 0; i < data.length; i++) {
        let factor = data[i] ^ result[0];
        result.copyWithin(0, 1);
        result[ecLen - 1] = 0;
        for (let j = 0; j < ecLen; j++) {
            result[j] ^= GF256.mul(factor, genPoly(ecLen)[j]);
        }
    }
    return result;
}

function encodeAlphanumeric(text) {
    let bits = '0010';
    bits += text.length.toString(2).padStart(9, '0');
    for (let i = 0; i < text.length; i += 2) {
        if (i + 1 < text.length) {
            const v = 45 * ALPHANUMERIC_CHARSET.indexOf(text[i]) + ALPHANUMERIC_CHARSET.indexOf(text[i + 1]);
            bits += v.toString(2).padStart(11, '0');
        } else {
            const v = ALPHANUMERIC_CHARSET.indexOf(text[i]);
            bits += v.toString(2).padStart(6, '0');
        }
    }
    bits += '0000'; // Terminator
    return bits;
}

function applyMask(matrix, maskPattern) {
    const size = matrix.length;
    const masked = matrix.map(row => row.slice());
    for (let y = 0; y < size; y++) {
        for (let x = 0; x < size; x++) {
            if (typeof masked[y][x] === 'boolean') {
                let mask;
                switch (maskPattern) {
                    case 0: mask = (y + x) % 2 === 0; break;
                    case 1: mask = y % 2 === 0; break;
                    case 2: mask = x % 3 === 0; break;
                    case 3: mask = (y + x) % 3 === 0; break;
                    default: mask = false;
                }
                if (mask) masked[y][x] = !masked[y][x];
            }
        }
    }
    return masked;
}

function placeFinderPatterns(matrix) {
    const positions = [
        [0, 0],
        [0, matrix.length - 7],
        [matrix.length - 7, 0]
    ];
    for (const [y, x] of positions) {
        for (let dy = 0; dy < 7; dy++) {
            for (let dx = 0; dx < 7; dx++) {
                const isBorder = dx === 0 || dx === 6 || dy === 0 || dy === 6;
                const isCenter = dx >= 2 && dx <= 4 && dy >= 2 && dy <= 4;
                matrix[y + dy][x + dx] = isBorder || isCenter;
            }
        }
    }
}

function placeTimingPatterns(matrix) {
    for (let i = 8; i < matrix.length - 8; i++) {
        const bit = i % 2 === 0;
        if (matrix[6][i] === null) matrix[6][i] = bit;
        if (matrix[i][6] === null) matrix[i][6] = bit;
    }
}

function placeFormatInfo(matrix, maskPattern, eccLevel = 'Q') {
    const formatBits = {
        Q: ['111011111000100', '111001011110011', '111110110101010', '111100010011101']
    }[eccLevel][maskPattern];
    const size = matrix.length;

    for (let i = 0; i < 15; i++) {
        const bit = formatBits[i] === '1';
        // Format info around top-left
        if (i < 6) matrix[8][i] = bit;
        else if (i < 8) matrix[8][i + 1] = bit;
        else matrix[8][size - 15 + i] = bit;

        if (i < 8) matrix[i][8] = bit;
        else if (i < 9) matrix[i + 1][8] = bit;
        else matrix[size - 15 + i][8] = bit;
    }
}

function buildMatrix(dataBits, size = 21) {
    const matrix = Array.from({ length: size }, () => Array(size).fill(null));

    // Draw position detection patterns
    drawFinderPattern(matrix, 0, 0);
    drawFinderPattern(matrix, size - 7, 0);
    drawFinderPattern(matrix, 0, size - 7);

    // Draw timing patterns
    for (let i = 8; i < size - 8; i++) {
        matrix[6][i] = matrix[i][6] = i % 2 === 0;
    }

    // Reserve format info area
    for (let i = 0; i < 9; i++) {
        if (matrix[8][i] === null) matrix[8][i] = false;
        if (matrix[i][8] === null) matrix[i][8] = false;
    }
    for (let i = size - 8; i < size; i++) {
        if (matrix[8][i] === null) matrix[8][i] = false;
        if (matrix[i][8] === null) matrix[i][8] = false;
    }

    // Data placement (simplified zigzag)
    let dirUp = true;
    let col = size - 1;
    let bitIndex = 0;
    while (col > 0) {
        if (col === 6) col--; // Skip vertical timing pattern
        for (let row = 0; row < size; row++) {
            const y = dirUp ? size - 1 - row : row;
            for (let c = 0; c < 2; c++) {
                const x = col - c;
                if (matrix[y][x] === null) {
                    matrix[y][x] = dataBits[bitIndex++] === '1';
                }
            }
        }
        col -= 2;
        dirUp = !dirUp;
    }
    
    // Write the format info
    writeFormatInfo(matrix, '111011111000100');

    return matrix;
}

function drawMatrix(matrix, foreground = '#000000', background = '#ffffff') {
    const padding = 4;
    const size = matrix.length + padding * 2;
    const scale = 6;
    const canvas = document.createElement('canvas');
    canvas.width = canvas.height = size * scale;
    const ctx = canvas.getContext('2d');

    ctx.fillStyle = background;
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.fillStyle = foreground;
    for (let y = 0; y < matrix.length; y++) {
        for (let x = 0; x < matrix.length; x++) {
            if (matrix[y][x]) {
                ctx.fillRect((x + padding) * scale, (y + padding) * scale, scale, scale);
            }
        }
    }

    return canvas.toDataURL();
}

function drawFinderPattern(matrix, x, y) {
    const pattern = [
        [1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1],
    ];
    for (let dy = 0; dy < 7; dy++) {
        for (let dx = 0; dx < 7; dx++) {
            matrix[y + dy][x + dx] = !!pattern[dy][dx];
        }
    }
}

function writeFormatInfo(matrix, formatBits) {
    const size = matrix.length;
    const positions = [
        // Top-left
        [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [7, 8], [8, 8],
        [8, 7], [8, 5], [8, 4], [8, 3], [8, 2], [8, 1], [8, 0],
        // Mirror format bits (bottom-left and top-right)
        [size - 1, 8], [size - 2, 8], [size - 3, 8], [size - 4, 8],
        [size - 5, 8], [size - 6, 8], [size - 7, 8], [8, size - 8],
        [8, size - 7], [8, size - 6], [8, size - 5], [8, size - 4],
        [8, size - 3], [8, size - 2], [8, size - 1]
    ];

    const bits = formatBits.padStart(15, '0');
    const formatCoords = [
        [0, 8], [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [7, 8], [8, 8],
        [8, 7], [8, 5], [8, 4], [8, 3], [8, 2], [8, 1], [8, 0],
        [8, size - 1], [8, size - 2], [8, size - 3], [8, size - 4],
        [8, size - 5], [8, size - 6], [8, size - 7],
        [size - 1, 8], [size - 2, 8], [size - 3, 8], [size - 4, 8],
        [size - 5, 8], [size - 6, 8], [size - 7, 8]
    ];

    for (let i = 0; i < 15; i++) {
        const [r, c] = formatCoords[i];
        matrix[r][c] = bits[i] === '1';
    }
}

function generateQRCode(text, eccLevel = 'Q', foreground = '#000000', background = '#ffffff') {
    const ecc = ECC_LEVELS[eccLevel];
    if (!ecc) throw new Error("Unsupported ECC level");

    const bitString = encodeAlphanumeric(text);
    const dataBytes = [];
    for (let i = 0; i < bitString.length; i += 8) {
        dataBytes.push(parseInt(bitString.slice(i, i + 8).padEnd(8, '0'), 2));
    }

    while (dataBytes.length < 19 - ecc.ecCodewordsPerBlock) {
        dataBytes.push(dataBytes.length % 2 ? 0x11 : 0xec);
    }

    const ec = reedSolomonEncode(dataBytes, ecc.ecCodewordsPerBlock);
    const fullData = [...dataBytes, ...ec];
    const fullBits = fullData.map(b => b.toString(2).padStart(8, '0')).join('');
    const matrix = buildMatrix(fullBits);
    return drawMatrix(matrix, foreground, background);
}