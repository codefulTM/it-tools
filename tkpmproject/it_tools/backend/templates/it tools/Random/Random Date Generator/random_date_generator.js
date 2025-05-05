const dateTimeFormat = document.getElementById('date-time-format');
const timeZone = document.getElementById('time-zone');
const dateTimeOutput = document.getElementById('date-time-output');
const generateDate = document.getElementById('generate-date');
const copyDate = document.getElementById('copy-date');

function padZero(n, length = 2) {
    return String(n).padStart(length, '0');
}

function formatDate(date, formatStr) {
    const hours24 = date.getHours();
    const hours12 = hours24 % 12 || 12;
    const ampm = hours24 >= 12 ? 'PM' : 'AM';

    const replacements = {
        'dd': padZero(date.getDate()),
        'MM': padZero(date.getMonth() + 1),
        'yyyy': date.getFullYear(),
        'hh': padZero(formatStr.includes('aa') ? hours12 : hours24),
        'mm': padZero(date.getMinutes()),
        'ss': padZero(date.getSeconds()),
        'aa': ampm,
        'zzz': Intl.DateTimeFormat().resolvedOptions().timeZone // Timezone if needed
    };

    return formatStr.replace(/dd|MM|yyyy|hh|mm|ss|aa|zzz/g, match => replacements[match]);
}

generateDate.addEventListener('click', () => {
    try {
        const startDate = new Date(1980, 1, 1);
        const endDate = new Date(2100, 1, 1);
        const dateTime = new Date(startDate.getTime() + Math.random() * (endDate.getTime() - startDate.getTime()));
        
        let format = dateTimeFormat.value;
        if (timeZone.checked) {
            format += ' zzz';
        }

        const formatted = formatDate(dateTime, format);
        console.log('Date/Time:', formatted);
        dateTimeOutput.value = formatted;
    } catch (err) {
        console.error('Failed to generate random date/time', err);
        alert('Failed to generate random date/time');
    }
});

copyDate.addEventListener('click', async () => {
    if (!dateTimeOutput || dateTimeOutput.value === '') {
        alert('Please generate date/time first!');
        return;
    }
    try {
        await navigator.clipboard.writeText(dateTimeOutput.value);
        alert('Copied date/time to the clipboard successfully!');
    } catch (err) {
        console.error('Failed to copy date/time to the clipboard', err);
        alert('Failed to copy date/time to the clipboard');
    }
});
