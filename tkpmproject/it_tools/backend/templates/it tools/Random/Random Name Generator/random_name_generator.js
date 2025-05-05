const decreaseBtn = document.getElementById('decrease-btn');
const increaseBtn = document.getElementById('increase-btn');
const nameLengthInput = document.getElementById('name-length');
const firstLetterInput = document.getElementById('first-letter');
const fromLabel = document.getElementById('from-label');
const fromLetterInput = document.getElementById('from-letter');
const toLabel = document.getElementById('to-label');
const toLetterInput = document.getElementById('to-letter');
const singleLabel = document.getElementById('single-label');
const singleLetterInput = document.getElementById('single-letter');
const nameOutput = document.getElementById('output');
const generateButton = document.getElementById('generate-name');
const copyButton = document.getElementById('copy-name');

const minLength = 3;
const maxLength = 8;

decreaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    let nameLength = parseInt(nameLengthInput.value, 10);
    if (!isNaN(nameLength)) {
        nameLengthInput.value = Math.max(minLength, nameLength - 1);
    }
});

increaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    let nameLength = parseInt(nameLengthInput.value, 10);
    if (!isNaN(nameLength)) {
        nameLengthInput.value = Math.min(nameLength + 1, maxLength);
    }
});

fromLetterInput.addEventListener('input', (e) => {
    const value = e.target.value.toUpperCase();
    fromLetterInput.value = value;
});

toLetterInput.addEventListener('input', (e) => {
    const value = e.target.value.toUpperCase();
    toLetterInput.value = value;
});

singleLetterInput.addEventListener('input', (e) => {
    const value = e.target.value.toUpperCase();
    singleLetterInput.value = value;
});

firstLetterInput.addEventListener('change', (e) => {
    const value = e.target.value;
    if (value === 'from-to') {
        fromLabel.removeAttribute('hidden');
        fromLetterInput.removeAttribute('hidden');
        fromLetterInput.setAttribute('required', true);

        toLabel.removeAttribute('hidden');
        toLetterInput.removeAttribute('hidden');
        toLetterInput.setAttribute('required', true);

        singleLabel.setAttribute('hidden', true);
        singleLetterInput.setAttribute('hidden', true);
        singleLetterInput.removeAttribute('required');
    } else if (value === 'single') {
        fromLabel.setAttribute('hidden', true);
        fromLetterInput.setAttribute('hidden', true);
        fromLetterInput.removeAttribute('required');

        toLabel.setAttribute('hidden', true);
        toLetterInput.setAttribute('hidden', true);
        toLetterInput.removeAttribute('required');

        singleLabel.removeAttribute('hidden');
        singleLetterInput.removeAttribute('hidden');
        singleLetterInput.setAttribute('required', true);
    }
});

nameLengthInput.addEventListener('change', () => {
    if (nameLengthInput.value < minLength) {
        nameLengthInput.value = minLength;
    }
    else if (nameLengthInput.value > maxLength) {
        nameLengthInput.value = maxLength;
    }
});

generateButton.addEventListener('click', () => {
    try {
        let randomName = '';
        let attempts = 0;
        const maxAttempts = 1000000;
        const nameLength = parseInt(nameLengthInput.value, 10);

        if (firstLetterInput.value == 'single') {
            if (!isAlphabet(singleLetterInput.value)) {
                alert('Please type the single letter filter for the first letter first!');
                return;
            }
            do {
                attempts++;
                if (attempts > maxAttempts) {
                    alert('Sorry, the tool took too long to generate random name. Please try again');
                    return;
                }
                randomName = generateRandomName(nameLength);
            } while (randomName.charAt(0) !== singleLetterInput.value);
        }

        else if (firstLetterInput.value == 'from-to') {
            if (!isAlphabet(fromLetterInput.value) || !isAlphabet(toLetterInput.value)) {
                alert('Please type the range from-to letter for the first letter first!');
                return;
            }
            const fromChar = fromLetterInput.value.charAt(0);
            const toChar = toLetterInput.value.charAt(0);
            if (fromChar > toChar) {
                alert('From letter must come before To letter!');
                return;
            }
            do {
                attempts++;
                if (attempts > maxAttempts) {
                    alert('Sorry, the tool took too long to generate random name. Please try again');
                    return;
                }
                randomName = generateRandomName(nameLength);
            } while (randomName.charAt(0) < fromChar || randomName.charAt(0) > toChar);
        }

        console.log('Attempts:', attempts);
        nameOutput.value = randomName;
    } catch (err) {
        console.error('Failed to generate random name', err);
        alert('Failed to generate random name');
    }
});

copyButton.addEventListener('click', async () => {
    if (!nameOutput || nameOutput.value === '') {
        alert('Please generate name first!');
        return;
    }
    try {
        await navigator.clipboard.writeText(nameOutput.value);
        alert('Name copied to the clipboard successfully!');
    } catch (err) {
        console.error('Failed to copy name to the clipboard', err);
        alert('Failed to copy name to the clipboard');
    }
});

function isAlphabet(str) {
    return /^[a-zA-Z]$/.test(str);
}

function generateRandomName(length) {
    const syllables = ['ba','be','bi','bo','bu','ca','ce','ci','co','cu','da','de','di','do','du',
                        'fa','fe','fi','fo','fu','ga','ge','gi','go','gu','ha','he','hi','ho','hu',
                        'ja','je','ji','jo','ju','ka','ke','ki','ko','ku','la','le','li','lo','lu',
                        'ma','me','mi','mo','mu','na','ne','ni','no','nu','pa','pe','pi','po','pu',
                        'ra','re','ri','ro','ru','sa','se','si','so','su','ta','te','ti','to','tu'];

    let name = '';
    while (name.length < length) {
        const syllable = syllables[Math.floor(Math.random() * syllables.length)];
        name += syllable;
    }
    name = name.slice(0, length);
    return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
}