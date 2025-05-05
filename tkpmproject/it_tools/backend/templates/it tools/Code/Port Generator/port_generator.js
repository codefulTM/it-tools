const randomPort = document.getElementById("port");
const generatePort = document.getElementById("generate-port");
const refreshPort = document.getElementById("refresh-port");

const defaultPort = 10000;
const fromPort = 1024;
const toPort = 65535;

randomPort.textContent = defaultPort;

generatePort.addEventListener ("click", () => {
    randomPort.textContent = Math.floor((Math.random() * (toPort - fromPort))) + fromPort
});

refreshPort.addEventListener ("click", () => {
    randomPort.textContent = defaultPort;
});