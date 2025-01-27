const base_url = 'https://l5xwzx0n-5000.inc1.devtunnels.ms';

document.getElementById('encrypt').addEventListener('click', async () => {
    let plain_text = document.getElementById('plain_text').value;
    let key = document.getElementById('key').value;

    const cipher = document.getElementById('cipher').value;
// console.log(cipher)
    if (cipher === 'vigenere') {
        try {
            const response = await fetch(`${base_url}/vignere-encrypt`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: plain_text, key: key })
            });

            if (response.ok) {
                const data = await response.json();
                document.getElementById('output').innerText = data.encrypted_text || "Encryption successful!";
            } else {
                document.getElementById('output').innerText = "Error in encryption!";
            }
        } catch (error) {
            document.getElementById('output').innerText = "Failed to connect to the server.";
        }
    }
    else if (cipher === 'playfair') {
        try {
            const response = await fetch(`${base_url}/playfair-encrypt`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: plain_text, key: key })
            });

            if (response.ok) {
                const data = await response.json();
                document.getElementById('output').innerText = data.encrypted_text || "Encryption successful!";
            } else {
                document.getElementById('output').innerText = "Error in encryption!";
            }
        } catch (error) {
            document.getElementById('output').innerText = "Failed to connect to the server.";
        }
    }
});



document.getElementById('decrypt').addEventListener('click', async () => {
    let plain_text = document.getElementById('plain_text').value;
    let key = document.getElementById('key').value;

    const cipher = document.getElementById('cipher').value;
// console.log(cipher)
    if (cipher === 'vigenere') {
        try {
            const response = await fetch(`${base_url}/vignere-decrypt`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: plain_text, key: key })
            });

            if (response.ok) {
                const data = await response.json();
                document.getElementById('output').innerText = data.plain_text || "Decryption successful!";
            } else {
                document.getElementById('output').innerText = "Error in decryption!";
            }
        } catch (error) {
            document.getElementById('output').innerText = "Failed to connect to the server.";
        }
    }
    else if (cipher === 'playfair') {
        try {
            const response = await fetch(`${base_url}/playfair-decrypt`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: plain_text, key: key })
            });

            if (response.ok) {
                const data = await response.json();
                document.getElementById('output').innerText = data.decrypted_text || "Decryption successful!";
            } else {
                document.getElementById('output').innerText = "Error in decryption!";
            }
        } catch (error) {
            document.getElementById('output').innerText = "Failed to connect to the server.";
        }
    }
});