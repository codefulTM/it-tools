const algorithms = {
    MD5: CryptoJS.MD5,
    SHA1: CryptoJS.SHA1,
    SHA256: CryptoJS.SHA256,
    SHA224: CryptoJS.SHA224,
    SHA512: CryptoJS.SHA512,
    SHA384: CryptoJS.SHA384,
    SHA3: CryptoJS.SHA3,
    RIPEMD160: CryptoJS.RIPEMD160,
};

const input = document.getElementById("input");
const results = document.getElementById("results");

input.addEventListener("input", updateHashes);

function updateHashes() {
    const text = input.value;
    results.innerHTML = "";

    Object.entries(algorithms).forEach(([name, func]) => {
        const hash = func(text).toString(CryptoJS.enc.Hex);

        const row = document.createElement("div");
        row.style.display = "flex";
        row.style.alignItems = "center";
        row.style.marginBottom = "10px";
        row.style.gap = "10px";

        const label = document.createElement("div");
        label.style.width = "80px";
        label.textContent = name;

        const value = document.createElement("input");
        value.value = hash;
        value.readOnly = true;
        value.style.flex = "1";
        value.style.padding = "8px";
        value.style.background = "#2a2a2a";
        value.style.color = "#00ffb3";
        value.style.border = "none";
        value.style.borderRadius = "5px";
        value.style.fontFamily = "monospace";

        const copyBtn = document.createElement("button");
        copyBtn.textContent = "📋";
        copyBtn.style.padding = "8px";
        copyBtn.style.background = "#444";
        copyBtn.style.color = "white";
        copyBtn.style.border = "none";
        copyBtn.style.borderRadius = "5px";
        copyBtn.style.cursor = "pointer";

        copyBtn.onclick = () => {
            value.select();
            document.execCommand("copy");
            alert("Copied!")
        };

        row.appendChild(label);
        row.appendChild(value);
        row.appendChild(copyBtn);
        results.appendChild(row);
    });
}

// Initial run
updateHashes();