function convert(conversionType) {
    var unicode = document.getElementsByName('unicode')[0].value;
    fetch('/convert', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ type: conversionType, text: unicode })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementsByName('bijoy')[0].value = data.result;
    });
}