const unitType = document.getElementById("unit-type");

const meter = document.getElementById("meter");
const meterDecrease = document.getElementById("meter-decrease-btn");
const meterIncrease = document.getElementById("meter-increase-btn");

const inch = document.getElementById("inch");
const inchDecrease = document.getElementById("inch-decrease-btn");
const inchIncrease = document.getElementById("inch-increase-btn");

const yard = document.getElementById("yard");
const yardDecrease = document.getElementById("yard-decrease-btn");  
const yardIncrease = document.getElementById("yard-increase-btn"); 

const kilogram = document.getElementById("kilogram");
const kilogramDecrease = document.getElementById("kilogram-decrease-btn");
const kilogramIncrease = document.getElementById("kilogram-increase-btn");

const pound = document.getElementById("pound");
const poundDecrease = document.getElementById("pound-decrease-btn");
const poundIncrease = document.getElementById("pound-increase-btn");

const ounce = document.getElementById("ounce");
const ounceDecrease = document.getElementById("ounce-decrease-btn");
const ounceIncrease = document.getElementById("ounce-increase-btn");

const celsius = document.getElementById("celsius");
const celsiusDecrease = document.getElementById("celsius-decrease-btn");
const celsiusIncrease = document.getElementById("celsius-increase-btn");

const fahrenheit = document.getElementById("fahrenheit");
const fahrenheitDecrease = document.getElementById("fahrenheit-decrease-btn");
const fahrenheitIncrease = document.getElementById("fahrenheit-increase-btn");

const kelvin = document.getElementById("kelvin");
const kelvinDecrease = document.getElementById("kelvin-decrease-btn");
const kelvinIncrease = document.getElementById("kelvin-increase-btn");

const pascal = document.getElementById("pascal");
const pascalDecrease = document.getElementById("pascal-decrease-btn");
const pascalIncrease = document.getElementById("pascal-increase-btn");

const atm = document.getElementById("atm");
const atmDecrease = document.getElementById("atm-decrease-btn");
const atmIncrease = document.getElementById("atm-increase-btn");

const mmHg = document.getElementById("mmHg");
const mmHgDecrease = document.getElementById("mmHg-decrease-btn");
const mmHgIncrease = document.getElementById("mmHg-increase-btn");

function decreaseValue(element, min) {
    let value = parseFloat(element.value);
    if (value > min + 1) {
        value -= 1;
        element.value = value.toFixed(2);
    }
    return value;
}

function increaseValue(element, max) {
    let value = parseFloat(element.value);
    if (value < max - 1) {
        value += 1;
        element.value = value.toFixed(2);
    }
    return value;
}

meterDecrease.addEventListener("click", function() {
    let meterValue = decreaseValue(meter, 0);
    inch.value = (parseFloat(meterValue) * 39.3701).toFixed(2);
    yard.value = (parseFloat(meterValue) * 1.09361).toFixed(2);
});

meterIncrease.addEventListener("click", function() {
    let meterValue = increaseValue(meter, 1000000);
    inch.value = (parseFloat(meterValue) * 39.3701).toFixed(2);
    yard.value = (parseFloat(meterValue) * 1.09361).toFixed(2);
});

inchDecrease.addEventListener("click", function() {
    let inchValue = decreaseValue(inch, 0);
    meter.value = (parseFloat(inchValue) / 39.3701).toFixed(2);
    yard.value = (parseFloat(inchValue) / 36).toFixed(2);
});

inchIncrease.addEventListener("click", function() {
    let inchValue = increaseValue(inch, 1000000);
    meter.value = (parseFloat(inchValue) / 39.3701).toFixed(2);
    yard.value = (parseFloat(inchValue) / 36).toFixed(2);
});

yardDecrease.addEventListener("click", function() {
    let yardValue = decreaseValue(yard, 0);
    meter.value = (parseFloat(yardValue) / 1.09361).toFixed(2);
    inch.value = (parseFloat(yardValue) * 36).toFixed(2);
});

yardIncrease.addEventListener("click", function() {
    let yardValue = increaseValue(yard, 1000000);
    meter.value = (parseFloat(yardValue) / 1.09361).toFixed(2);
    inch.value = (parseFloat(yardValue) * 36).toFixed(2);
});

kilogramDecrease.addEventListener("click", function() {
    let kilogramValue = decreaseValue(kilogram, 0);
    pound.value = (parseFloat(kilogramValue) * 2.20462).toFixed(2);
    ounce.value = (parseFloat(kilogramValue) * 35.274).toFixed(2);
});

kilogramIncrease.addEventListener("click", function() {
    let kilogramValue = increaseValue(kilogram, 1000000);
    pound.value = (parseFloat(kilogramValue) * 2.20462).toFixed(2);
    ounce.value = (parseFloat(kilogramValue) * 35.274).toFixed(2);
});

poundDecrease.addEventListener("click", function() {
    let poundValue = decreaseValue(pound, 0);
    kilogram.value = (parseFloat(poundValue) / 2.20462).toFixed(2);
    ounce.value = (parseFloat(poundValue) * 16).toFixed(2);
});

poundIncrease.addEventListener("click", function() {
    let poundValue = increaseValue(pound, 1000000);
    kilogram.value = (parseFloat(poundValue) / 2.20462).toFixed(2);
    ounce.value = (parseFloat(poundValue) * 16).toFixed(2);
});

ounceDecrease.addEventListener("click", function() {
    let ounceValue = decreaseValue(ounce, 0);
    kilogram.value = (parseFloat(ounceValue) / 35.274).toFixed(2);
    pound.value = (parseFloat(ounceValue) / 16).toFixed(2);
});

ounceIncrease.addEventListener("click", function() {
    let ounceValue = increaseValue(ounce, 1000000);
    kilogram.value = (parseFloat(ounceValue) / 35.274).toFixed(2);
    pound.value = (parseFloat(ounceValue) / 16).toFixed(2);
});

celsiusDecrease.addEventListener("click", function() {
    let celsiusValue = decreaseValue(celsius, -273.15);
    fahrenheit.value = (parseFloat(celsiusValue) * 9/5 + 32).toFixed(2);
    kelvin.value = (parseFloat(celsiusValue) + 273.15).toFixed(2);
});

celsiusIncrease.addEventListener("click", function() {
    let celsiusValue = increaseValue(celsius, 1000000);
    fahrenheit.value = (parseFloat(celsiusValue) * 9/5 + 32).toFixed(2);
    kelvin.value = (parseFloat(celsiusValue) + 273.15).toFixed(2);
});

fahrenheitDecrease.addEventListener("click", function() {
    let fahrenheitValue = decreaseValue(fahrenheit, -459.67);
    celsius.value = ((parseFloat(fahrenheitValue) - 32) * 5/9).toFixed(2);
    kelvin.value = ((parseFloat(fahrenheitValue) - 32) * 5/9 + 273.15).toFixed(2);
});

fahrenheitIncrease.addEventListener("click", function() {
    let fahrenheitValue = increaseValue(fahrenheit, 1000000);
    celsius.value = ((parseFloat(fahrenheitValue) - 32) * 5/9).toFixed(2);
    kelvin.value = ((parseFloat(fahrenheitValue) - 32) * 5/9 + 273.15).toFixed(2);
});

kelvinDecrease.addEventListener("click", function() {
    let kelvinValue = decreaseValue(kelvin, 0);
    celsius.value = (parseFloat(kelvinValue) - 273.15).toFixed(2);
    fahrenheit.value = ((parseFloat(kelvinValue) - 273.15) * 9/5 + 32).toFixed(2);
});

kelvinIncrease.addEventListener("click", function() {
    increaseValue(kelvin, 1000000);
    celsius.value = (parseFloat(kelvin.value) - 273.15).toFixed(2);
    fahrenheit.value = ((parseFloat(kelvin.value) - 273.15) * 9/5 + 32).toFixed(2);
});

pascalDecrease.addEventListener("click", function() {
    decreaseValue(pascal, 0);
    atm.value = (parseFloat(pascal.value) / 101325).toFixed(2);
    mmHg.value = (parseFloat(pascal.value) / 133.322).toFixed(2);
});

pascalIncrease.addEventListener("click", function() {
    increaseValue(pascal, 1000000);
    atm.value = (parseFloat(pascal.value) / 101325).toFixed(2);
    mmHg.value = (parseFloat(pascal.value) / 133.322).toFixed(2);
});

atmDecrease.addEventListener("click", function() {
    decreaseValue(mmHg, 0);
    pascal.value = (parseFloat(mmHg.value) * 133.322).toFixed(2);
    atm.value = (parseFloat(mmHg.value) / 760).toFixed(2);
});

atmIncrease.addEventListener("click", function() {
    increaseValue(atm, 1000000);
    pascal.value = (parseFloat(atm.value) * 101325).toFixed(2);
    mmHg.value = (parseFloat(atm.value) * 760).toFixed(2);
});

mmHgDecrease.addEventListener("click", function() {
    decreaseValue(mmHg, 0);
    pascal.value = (parseFloat(mmHg.value) * 133.322).toFixed(2);
    atm.value = (parseFloat(mmHg.value) / 760).toFixed(2);
});

mmHgIncrease.addEventListener("click", function() {
    increaseValue(mmHg, 1000000);
    pascal.value = (parseFloat(mmHg.value) * 133.322).toFixed(2);
    atm.value = (parseFloat(mmHg.value) / 760).toFixed(2);
});

function changeUnitType() {
    const selectedUnit = unitType.value;
    const units = {
        "length": ["meter", "inch", "yard"],
        "weight": ["kilogram", "pound", "ounce"],
        "temperature": ["celsius", "fahrenheit", "kelvin"],
        "pressure": ["pascal", "atm", "mmHg"]
    };

    for (const unitGroup in units) {
        if (unitGroup === selectedUnit) {
            for (const unit of units[unitGroup]) {
                document.getElementById(unit.concat("-container")).removeAttribute("hidden");
                document.getElementById(unit.concat("-label")).removeAttribute("hidden");
            }
        }
        else {
            for (const unit of units[unitGroup]) {
                document.getElementById(unit.concat("-container")).setAttribute("hidden", true);
                document.getElementById(unit.concat("-label")).setAttribute("hidden", true);
            }
        }
    }
}

unitType.addEventListener("change", function() {
    changeUnitType(); // Call the function when the unit type changes
});

document.addEventListener("DOMContentLoaded", function() {
    changeUnitType(); // Call the function on page load to set the initial state
});
