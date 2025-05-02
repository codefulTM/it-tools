
from backend.classes.ToolComponent import ToolComponent

class Tool9(ToolComponent):
    def get_info(self):
        return {
            'id': 9,
            'name': 'Hash Text',
            'description': 'A tool that hashes text.',
            'category': 'Crypto',
            'is_premium': False,
            'is_enabled': True
        }

    def get_html(self):
        return """<h2 style="margin-bottom:10px;">Hash text</h2>

<p style="color:#aaa;">Hash a text string using the function you need: MD5, SHA1, SHA256, SHA224, SHA512, SHA384, SHA3

    or RIPEMD160</p>



<!-- Input -->

<textarea id="input" placeholder="Your string to hash..." rows="4"

    style="width:100%; padding:10px; margin:15px 0; background:#2a2a2a; color:#fff; border:none; border-radius:5px;"></textarea>



<!-- Digest Encoding -->

<label for="encoding">Digest encoding</label>

<select id="encoding"

    style="width:100%; padding:10px; margin:10px 0 20px 0; background:#2a2a2a; color:white; border:none; border-radius:5px;">

    <option value="hex">Hexadecimal (base 16)</option>

    <!-- Future support: base64, binary,... -->

</select>



<!-- Output list -->

<div id="results"></div>



<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js"></script>"""

    def get_js(self):
        return """const algorithms = {

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

updateHashes();"""
        