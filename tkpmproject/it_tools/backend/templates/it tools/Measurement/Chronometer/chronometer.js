const startButton = document.getElementById('start-btn');
const stopButton = document.getElementById('stop-btn');
const resetButton = document.getElementById('reset-btn');

startButton.addEventListener('click', function() {
    startButton.setAttribute('hidden', true);
    stopButton.removeAttribute('hidden');
});

stopButton.addEventListener('click', function() {
    startButton.removeAttribute('hidden');
    stopButton.setAttribute('hidden', true);
});

resetButton.addEventListener('click', function() {
    startButton.removeAttribute('hidden');
    stopButton.setAttribute('hidden', true);
});