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

decreaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    let nameLength = parseInt(nameLengthInput.value, 10);
    if (!isNaN(nameLength)) {
        nameLengthInput.value = Math.max(1, nameLength - 1);
    }
});

increaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    let nameLength = parseInt(nameLengthInput.value, 10);
    if (!isNaN(nameLength)) {
        nameLengthInput.value = Math.min(nameLength + 1, 100);
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
        singleLabel.removeAttribute('required');
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