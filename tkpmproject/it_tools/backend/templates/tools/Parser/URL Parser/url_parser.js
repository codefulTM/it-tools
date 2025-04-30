function parseUrl() {
    const input = document.getElementById('urlInput').value;
    const output = document.getElementById('output');

    try {
        const url = new URL(input);
        const params = [...url.searchParams.entries()];
        const makeRow = (label, value) => `
      <div style="margin-bottom: 0.5rem;">
        <strong style="display: inline-block; width: 100px;">${label}:</strong>
        <input value="${value}" readonly style="width: 70%; padding: 4px; background: #222; color: white; border: 1px solid #333;" />
      </div>
    `;

        let result = '';
        result += makeRow('Protocol', url.protocol.replace(':', ''));
        result += makeRow('Username', url.username);
        result += makeRow('Password', url.password);
        result += makeRow('Hostname', url.hostname);
        result += makeRow('Port', url.port);
        result += makeRow('Path', url.pathname);
        result += makeRow('Params', url.search);
        if (params.length > 0) {
            result += `<div style="margin: 1rem 0 0.5rem;"><strong>↳ Query Params:</strong></div>`;
            params.forEach(([key, value]) => {
                result += makeRow('↳ ' + key, value);
            });
        }
        result += makeRow('Hash', url.hash.replace('#', ''));

        output.innerHTML = result;
    } catch (e) {
        output.innerHTML = `<span style="color: red;">Invalid URL</span>`;
    }
}

window.onload = parseUrl;