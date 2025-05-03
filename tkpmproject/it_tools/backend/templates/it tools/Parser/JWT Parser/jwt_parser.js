function base64UrlDecode(str) {
    // Replace URL-safe chars, pad to multiple of 4, then atob + decodeURIComponent
    str = str.replace(/-/g, '+').replace(/_/g, '/');
    str += '='.repeat((4 - str.length % 4) % 4);
    try {
        const bin = atob(str);
        return decodeURIComponent(bin.split('').map(c =>
            '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2)
        ).join(''));
    } catch {
        return null;
    }
}

function renderSection(title, obj) {
    if (!obj || typeof obj !== 'object') return '';
    let html = '';
    html += `<div style="margin-top:20px;"><h3 style="margin-bottom:10px;border-bottom:1px solid #333;padding-bottom:3px;">${title}</h3>`;
    for (let [k, v] of Object.entries(obj)) {
        html += `
<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #2a2a2a;">
<div style="min-width:80px;">${k}</div>
<div style="flex:1;text-align:right;word-break:break-all;">${v}</div>
</div>`;
    }
    html += `</div>`;
    return html;
}

function parseJWT() {
    const container = document.getElementById('result');
    const token = document.getElementById('jwt').value.trim();
    if (!token) {
        container.innerHTML = '';
        return;
    }
    const parts = token.split('.');
    if (parts.length < 2) {
        container.innerHTML = `<div style="color:#f55;margin-top:20px;">Invalid JWT</div>`;
        return;
    }

    const headerJson = base64UrlDecode(parts[0]);
    const payloadJson = base64UrlDecode(parts[1]);
    let header, payload;
    try {
        header = JSON.parse(headerJson);
        payload = JSON.parse(payloadJson);
    } catch {
        container.innerHTML = `<div style="color:#f55;margin-top:20px;">Failed to decode or parse JSON.</div>`;
        return;
    }

    let html = '';
    html += renderSection('Header', header);
    html += renderSection('Payload', payload);
    container.innerHTML = html;
}

document.getElementById('jwt').addEventListener('input', parseJWT);
window.addEventListener('load', parseJWT);