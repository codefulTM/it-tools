function isPrime(n) {
    if (n <= 1) return false;
    for (let i = 2; i * i <= n; i++) {
        if (n % i === 0) return false;
    }
    return true;
}

function primeFactors(n) {
    const factors = [];
    while (n % 2 === 0) {
        factors.push(2);
        n /= 2;
    }
    for (let i = 3; i <= Math.sqrt(n); i += 2) {
        while (n % i === 0) {
            factors.push(i);
            n /= i;
        }
    }
    if (n > 2) {
        factors.push(n);
    }
    return factors;
}

function isPerfectSquare(n) {
    return Number.isInteger(Math.sqrt(n));
}

function isPerfectCube(n) {
    return Number.isInteger(Math.cbrt(n));
}

function isPerfectNumber(n) {
    if (n <= 1) return false;
    let sum = 1;
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            sum += i;
            if (i !== n / i) sum += n / i;
        }
    }
    return sum === n;
}

function isFibonacci(n) {
    const isPerfectSquare = (x) => Number.isInteger(Math.sqrt(x));
    return isPerfectSquare(5 * n * n + 4) || isPerfectSquare(5 * n * n - 4);
}

function isCatalan(n) {
    // Catalan sequence: 1, 1, 2, 5, 14, 42, 132, 429, ...
    const catalan = [1];
    for (let i = 0; i < 20; i++) {
        catalan.push((2 * (2 * i + 1) * catalan[i]) / (i + 2));
    }
    return catalan.includes(n);
}

function isPell(n) {
    // Pell sequence: 0, 1, 2, 5, 12, 29, 70, 169, ...
    const pell = [0, 1];
    for (let i = 2; i < 30; i++) {
        pell[i] = 2 * pell[i - 1] + pell[i - 2];
    }
    return pell.includes(n);
}

function divisors(n) {
    const divs = [];
    for (let i = 1; i <= Math.floor(Math.sqrt(n)); i++) {
        if (n % i === 0) {
            divs.push(i);
            if (i !== n / i) divs.push(n / i);
        }
    }
    return divs.sort((a, b) => a - b);
}

function multiples(n, count = 5) {
    const mults = [];
    for (let i = 1; i <= count; i++) {
        mults.push(n * i);
    }
    return mults;
}

function analyzeNumber() {
    const num = parseInt(document.getElementById("numberInput").value);
    const resultDiv = document.getElementById("result");
    if (isNaN(num)) {
        resultDiv.innerHTML = "<b>Please enter a valid integer.</b>";
        resultDiv.style.display = "block";
        return;
    }

    const props = [];
    props.push(`<b>Number:</b> ${num}`);
    props.push(`<b>Even/Odd:</b> ${num % 2 === 0 ? "Even" : "Odd"}`);
    props.push(`<b>Divisors:</b> ${divisors(num).join(", ")}`);
    props.push(`<b>First 5 Multiples:</b> ${multiples(num).join(", ")}`);
    props.push(`<b>Prime:</b> ${isPrime(num) ? "Yes" : "No"}`);
    props.push(`<b>Prime Factors:</b> ${primeFactors(num).join(" × ")}`);
    props.push(`<b>Perfect Number:</b> ${isPerfectNumber(num) ? "Yes" : "No"}`);
    props.push(`<b>Perfect Square:</b> ${isPerfectSquare(num) ? "Yes" : "No"}`);
    props.push(`<b>Perfect Cube:</b> ${isPerfectCube(num) ? "Yes" : "No"}`);
    props.push(`<b>Fibonacci Number:</b> ${isFibonacci(num) ? "Yes" : "No"}`);
    props.push(`<b>Catalan Number:</b> ${isCatalan(num) ? "Yes" : "No"}`);
    props.push(`<b>Pell Number:</b> ${isPell(num) ? "Yes" : "No"}`);

    resultDiv.innerHTML = props.join("<br><br>");
    resultDiv.style.display = "block";
}