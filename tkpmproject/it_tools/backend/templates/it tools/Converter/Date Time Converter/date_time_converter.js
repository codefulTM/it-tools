const fields = {
    ts: document.getElementById("ts"),
    locale: document.getElementById("locale"),
    iso: document.getElementById("iso"),
    iso9075: document.getElementById("iso9075"),
    rfc3339: document.getElementById("rfc3339"),
    rfc7231: document.getElementById("rfc7231")
};

function pad(n) {
    return n.toString().padStart(2, '0');
}

function fromDate(date) {
    return {
        ts: date.getTime(),
        locale: date.toLocaleString(),
        iso: date.toISOString(),
        iso9075: `${date.getFullYear()}-${pad(date.getMonth() + 1)}-${pad(date.getDate())} ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}`,
        rfc3339: date.toISOString(),
        rfc7231: date.toUTCString()
    };
}

function tryParseDate(str) {
    if (!str) return null;

    // Try timestamp (ms)
    if (/^\d{12,}$/.test(str)) {
        const ts = parseInt(str);
        const d = new Date(ts);
        return isNaN(d.getTime()) ? null : d;
    }

    // ISO 9075 (yyyy-MM-dd HH:mm:ss)
    if (/^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$/.test(str)) {
        const [datePart, timePart] = str.split(' ');
        const [y, m, d] = datePart.split('-');
        const [h, min, s] = timePart.split(':');
        return new Date(`${y}-${m}-${d}T${h}:${min}:${s}`);
    }

    // Try other formats (ISO 8601, RFC 3339, RFC 7231, Locale)
    const d = new Date(str);
    return isNaN(d.getTime()) ? null : d;
}

function updateFrom(sourceKey) {
    const input = fields[sourceKey].value.trim();
    const date = tryParseDate(input);
    if (!date) return;

    const values = fromDate(date);

    for (const key in fields) {
        if (key !== sourceKey) {
            fields[key].value = values[key];
        }
    }
}

// Add event listeners
for (const key in fields) {
    fields[key].addEventListener('input', () => updateFrom(key));
}

function setNow() {
    const now = new Date();
    const values = fromDate(now);
    for (const key in fields) {
        fields[key].value = values[key];
    }
}

setNow(); // Initial value