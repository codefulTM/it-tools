function ipToInt(ip) {
    return ip.split('.').reduce((acc, oct) => (acc << 8) + parseInt(oct), 0);
}

function intToIp(int) {
    return [(int >>> 24), (int >> 16 & 255), (int >> 8 & 255), (int & 255)].join('.');
}

function calculate() {
    const input = document.getElementById('ipInput').value;
    const [ip, cidrStr] = input.split('/');
    const cidr = parseInt(cidrStr);
    if (!ip || isNaN(cidr) || cidr < 0 || cidr > 32) {
        document.getElementById('output').innerHTML = '<div style="background: #222; padding: 8px; border-radius: 5px;">Invalid input</div>';
        return;
    }

    const ipInt = ipToInt(ip);
    const netmaskInt = (0xFFFFFFFF << (32 - cidr)) >>> 0;
    const wildcardInt = ~netmaskInt >>> 0;
    const networkInt = ipInt & netmaskInt;
    const broadcastInt = networkInt | wildcardInt;
    const firstAddrInt = networkInt + 1;
    const lastAddrInt = broadcastInt - 1;

    const netmaskBin = netmaskInt.toString(2).padStart(32, '0').match(/.{8}/g).join('.');
    const netmask = intToIp(netmaskInt);
    const wildcard = intToIp(wildcardInt);
    const network = intToIp(networkInt);
    const broadcast = intToIp(broadcastInt);
    const first = intToIp(firstAddrInt);
    const last = intToIp(lastAddrInt);
    const size = broadcastInt - networkInt + 1;

    const ipClass = (() => {
        const firstOctet = parseInt(ip.split('.')[0]);
        if (firstOctet < 128) return 'A';
        if (firstOctet < 192) return 'B';
        if (firstOctet < 224) return 'C';
        if (firstOctet < 240) return 'D';
        return 'E';
    })();

    const out = `
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">Netmask:</span> <span style="color: #fff;">${network}/${cidr}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">Network address:</span> <span style="color: #fff;">${network}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">Network mask:</span> <span style="color: #fff;">${netmask}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">Network mask in binary:</span> <span style="color: #fff;">${netmaskBin}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">CIDR notation:</span> <span style="color: #fff;">/${cidr}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">Wildcard mask:</span> <span style="color: #fff;">${wildcard}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">Network size:</span> <span style="color: #fff;">${size}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">First address:</span> <span style="color: #fff;">${first}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">Last address:</span> <span style="color: #fff;">${last}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">Broadcast address:</span> <span style="color: #fff;">${broadcast}</span></div>
<div style="background: #222; padding: 8px; border-radius: 5px; margin: 8px 0;"><span style="font-weight: bold; color: #aaa;">IP class:</span> <span style="color: #fff;">${ipClass}</span></div>
`;

    document.getElementById('output').innerHTML = out;
}

calculate();