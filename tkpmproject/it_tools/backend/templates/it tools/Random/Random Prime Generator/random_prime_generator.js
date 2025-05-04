const primeFromDecreaseBtn = document.getElementById('prime-from-decrease-btn');
const primeFromIncreaseBtn = document.getElementById('prime-from-increase-btn');
const primeToDecreaseBtn = document.getElementById('prime-to-decrease-btn');
const primtToIncreaseBtn = document.getElementById('prime-to-increase-btn');
const primeFromInput = document.getElementById('prime-from');
const primeToInput = document.getElementById('prime-to');

primeFromDecreaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    let primeFrom = parseInt(primeFromInput.value, 10);
    let primeTo = parseInt(primeToInput.value, 10);
    if (!isNaN(primeFrom) && !isNaN(primeTo)) {
        primeFromInput.value = Math.max(2, primeFrom - 1);
    }
});

primeFromIncreaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    let primeFrom = parseInt(primeFromInput.value, 10);
    let primeTo = parseInt(primeToInput.value, 10);
    if (!isNaN(primeFrom) && !isNaN(primeTo)) {
        primeFromInput.value = Math.min(primeFrom + 1, primeTo);
    }
});

primeToDecreaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    let primeFrom = parseInt(primeFromInput.value, 10);
    let primeTo = parseInt(primeToInput.value, 10);
    if (!isNaN(primeFrom) && !isNaN(primeTo)) {
        primeToInput.value = Math.max(primeFrom, primeTo - 1);
    }
});

primtToIncreaseBtn.addEventListener('click', (e) => {
    e.preventDefault();
    let primeFrom = parseInt(primeFromInput.value, 10);
    let primeTo = parseInt(primeToInput.value, 10);
    if (!isNaN(primeFrom) && !isNaN(primeTo)) {
        primeToInput.value = primeTo + 1;
    }
});

primeFromInput.addEventListener('change', (e) => {
    let primeFrom = parseInt(primeFromInput.value, 10);
    let primeTo = parseInt(primeToInput.value, 10);
    if (!isNaN(primeFrom) && !isNaN(primeTo)) {
        primeFrom = Math.max(primeFrom, 2);
        primeFromInput.value = primeFrom;
        primeTo = Math.max(primeFrom, primeTo);
        primeToInput.value = primeTo;
    }
});

primeToInput.addEventListener('change', (e) => {
    let primeFrom = parseInt(primeFromInput.value, 10);
    let primeTo = parseInt(primeToInput.value, 10);
    if (!isNaN(primeFrom) && !isNaN(primeTo)) {
        primeTo = Math.max(2, primeTo);
        primeToInput.value = primeTo;
        primeFrom = Math.min(primeTo, primeFrom);
        primeFromInput.value = primeFrom
    }
});