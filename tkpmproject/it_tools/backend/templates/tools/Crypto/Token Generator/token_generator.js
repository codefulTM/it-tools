function generateToken() {
    const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const lowercase = "abcdefghijklmnopqrstuvwxyz";
    const numbers = "0123456789";
    const symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?";

    let chars = "";
    if (document.getElementById("uppercase").checked) chars += uppercase;
    if (document.getElementById("lowercase").checked) chars += lowercase;
    if (document.getElementById("numbers").checked) chars += numbers;
    if (document.getElementById("symbols").checked) chars += symbols;

    const length = parseInt(document.getElementById("length").value);
    let password = "";

    for (let i = 0; i < length; i++) {
        password += chars.charAt(Math.floor(Math.random() * chars.length));
    }

    // Format password with line breaks (like the screenshot)
    let formatted = password.match(/.{1,64}/g).join('\n');
    document.getElementById("output").value = formatted;
}

function copyToken() {
    const output = document.getElementById("output");
    output.select();
    document.execCommand("copy");
    alert("Copied!");
    output.blur();
}

// Generate on load
generateToken();