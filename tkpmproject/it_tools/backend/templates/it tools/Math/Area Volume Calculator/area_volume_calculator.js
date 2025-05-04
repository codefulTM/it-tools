function showInputs() {
    const shape = document.getElementById("shape").value;
    const inputDiv = document.getElementById("inputs");
    inputDiv.innerHTML = "";

    const inputHTML = {
        circle: 'Radius: <input id="r" type="number" style="margin: 5px;">',
        triangle: 'Base: <input id="b" type="number" style="margin: 5px;"> Height: <input id="h" type="number" style="margin: 5px;">',
        rectangle: 'Width: <input id="w" type="number" style="margin: 5px;"> Height: <input id="h" type="number" style="margin: 5px;">',
        sphere: 'Radius: <input id="r" type="number" style="margin: 5px;">',
        cylinder: 'Radius: <input id="r" type="number" style="margin: 5px;"> Height: <input id="h" type="number" style="margin: 5px;">',
        cone: 'Radius: <input id="r" type="number" style="margin: 5px;"> Height: <input id="h" type="number" style="margin: 5px;">',
        box: 'Length: <input id="l" type="number" style="margin: 5px;"> Width: <input id="w" type="number" style="margin: 5px;"> Height: <input id="h" type="number" style="margin: 5px;">'
    };

    inputDiv.innerHTML = inputHTML[shape] || "";
    document.getElementById("result").innerHTML = "";
}

function calculate() {
    const shape = document.getElementById("shape").value;
    let result = 0;
    const π = Math.PI;

    try {
        switch (shape) {
            case "circle":
                let r = parseFloat(document.getElementById("r").value);
                result = π * r * r;
                showResult(`Area of Circle: ${result.toFixed(2)}`);
                break;
            case "triangle":
                let b = parseFloat(document.getElementById("b").value);
                let h1 = parseFloat(document.getElementById("h").value);
                result = 0.5 * b * h1;
                showResult(`Area of Triangle: ${result.toFixed(2)}`);
                break;
            case "rectangle":
                let w = parseFloat(document.getElementById("w").value);
                let h2 = parseFloat(document.getElementById("h").value);
                result = w * h2;
                showResult(`Area of Rectangle: ${result.toFixed(2)}`);
                break;
            case "sphere":
                let rs = parseFloat(document.getElementById("r").value);
                result = (4 / 3) * π * Math.pow(rs, 3);
                showResult(`Volume of Sphere: ${result.toFixed(2)}`);
                break;
            case "cylinder":
                let rc = parseFloat(document.getElementById("r").value);
                let hc = parseFloat(document.getElementById("h").value);
                result = π * rc * rc * hc;
                showResult(`Volume of Cylinder: ${result.toFixed(2)}`);
                break;
            case "cone":
                let rco = parseFloat(document.getElementById("r").value);
                let hco = parseFloat(document.getElementById("h").value);
                result = (1 / 3) * π * rco * rco * hco;
                showResult(`Volume of Cone: ${result.toFixed(2)}`);
                break;
            case "box":
                let l = parseFloat(document.getElementById("l").value);
                let wbox = parseFloat(document.getElementById("w").value);
                let hbox = parseFloat(document.getElementById("h").value);
                result = l * wbox * hbox;
                showResult(`Volume of Box: ${result.toFixed(2)}`);
                break;
            default:
                showResult("Please select a shape and fill in values.");
        }
    } catch (e) {
        showResult("⚠️ Error: Invalid input.");
    }
}

function showResult(text) {
    document.getElementById("result").innerHTML = text;
}