const hashString = document.getElementById('hashString');
const saltCount = document.getElementById('saltCount');
const hashOutput = document.getElementById('hashOutput');
const compareString = document.getElementById('compareString');
const compareHash = document.getElementById('compareHash');
const matchResult = document.getElementById('matchResult');

function generateHash() {
    const text = hashString.value || '';
    const rounds = parseInt(saltCount.value, 10) || 10;
    // sync version for simplicity
    const salt = dcodeIO.bcrypt.genSaltSync(rounds);
    const h = dcodeIO.bcrypt.hashSync(text, salt);
    hashOutput.value = h;
    compareHashes(); // update compare result if needed
}

function incSalt() {
    let v = parseInt(saltCount.value, 10) || 10;
    if (v < 16) saltCount.value = ++v;
    generateHash();
}
function decSalt() {
    let v = parseInt(saltCount.value, 10) || 10;
    if (v > 4) saltCount.value = --v;
    generateHash();
}

function copyHash() {
    hashOutput.select();
    document.execCommand('copy');
    alert("Copied!");
}

function compareHashes() {
    const txt = compareString.value || '';
    const hsh = compareHash.value || '';
    if (!txt || !hsh) {
        matchResult.textContent = 'No';
        matchResult.style.color = 'inherit';
        return;
    }
    const ok = dcodeIO.bcrypt.compareSync(txt, hsh);
    matchResult.textContent = ok ? 'Yes' : 'No';
    matchResult.style.color = ok ? '#0f0' : '#f44';
}

// listeners
hashString.addEventListener('input', generateHash);
saltCount.addEventListener('change', generateHash);
compareString.addEventListener('input', compareHashes);
compareHash.addEventListener('input', compareHashes);

// initial
generateHash();