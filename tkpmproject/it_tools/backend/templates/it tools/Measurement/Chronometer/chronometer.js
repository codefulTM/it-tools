const clock = document.getElementById("clock");
const startButton = document.getElementById("start-btn");
const stopButton = document.getElementById("stop-btn");
const resetButton = document.getElementById("reset-btn");

let startTime = 0;
let elapsedTime = 0;
let timerInterval = null;
let running = false;

startButton.addEventListener("click", function() {
    startButton.setAttribute("hidden", true);
    stopButton.removeAttribute("hidden");
    start();
});

stopButton.addEventListener("click", function() {
    startButton.removeAttribute("hidden");
    stopButton.setAttribute("hidden", true);
    stop();
});

resetButton.addEventListener("click", function() {
    startButton.removeAttribute("hidden");
    stopButton.setAttribute("hidden", true);
    reset();
});

function timeToString(time) {
    const milliseconds = Math.floor(time % 1000).toString().padStart(3, '0');
    const totalSeconds = Math.floor(time / 1000);
    const minutes = Math.floor(totalSeconds / 60).toString().padStart(2, '0');
    const seconds = (totalSeconds % 60).toString().padStart(2, '0');
    return `${minutes}:${seconds}.${milliseconds}`;
}

function updateDisplay() {
    const now = Date.now();
    elapsedTime = now - startTime;
    clock.textContent = timeToString(elapsedTime);
}

function start() {
    if (!running) {
        startTime = Date.now() - elapsedTime;
        timerInterval = setInterval(updateDisplay, 10);
        running = true;
    } else {
        stop();
    }
}

function stop() {
    clearInterval(timerInterval);
    running = false;
}

function reset() {
    clearInterval(timerInterval);
    startTime = 0;
    elapsedTime = 0;
    running = false;
    clock.textContent = "00:00.000";
}