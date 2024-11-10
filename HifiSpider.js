function base32Encode(str) {
    var base32chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";
    var bits = "";
    var base32 = "";

    for(var i = 0; i < str.length; i++) {
        var bit = str.charCodeAt(i).toString(2);
        while(bit.length < 8) {
            bit = "0" + bit;
        }
        bits += bit;
    }

    while(bits.length % 5 !== 0) {
        bits += "0";
    }

    for(var i = 0; i < bits.length; i += 5) {
        var chunk = bits.substring(i, i+5);
        base32 += base32chars[parseInt(chunk, 2)];
    }

    while(base32.length % 8 !== 0) {
        base32 += "=";
    }

    return base32.replace(/=/g, 'HiFiNiYINYUECICHANG');
}

function generateParam(data) {
    var key = '95wwwHiFiNicom27';
    var outText = '';

    for(var i = 0, j = 0; i < data.length; i++, j++) {
        if(j == key.length) j = 0;
        outText += String.fromCharCode(data.charCodeAt(i) ^ key.charCodeAt(j));
    }
    return base32Encode(outText);
}
