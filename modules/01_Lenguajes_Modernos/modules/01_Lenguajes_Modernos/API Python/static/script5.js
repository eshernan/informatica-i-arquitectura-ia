document.addEventListener('DOMContentLoaded', function() {
    // Referencias a elementos del DOM
    const colorCodeEl = document.getElementById('color-code');
    const saludoEl = document.getElementById('saludo');
    const copyBtn = document.getElementById('copy-button');
    const nombreInput = document.getElementById('nombre-input');
    const saludarBtn = document.getElementById('saludar-button');

    // --- Función para actualizar el color en la página ---
    function actualizarColor(color) {
        document.body.style.backgroundColor = color;
        colorCodeEl.textContent = color;
    }

    // --- Copiar al portapapeles con fallback (para HTTP) ---
    async function copiarTexto(texto) {
        try {
            await navigator.clipboard.writeText(texto);
            console.log('Copiado con clipboard API');
            return true;
        } catch (err) {
            console.warn('Clipboard API falló, usando fallback', err);
            // Fallback con execCommand
            const temp = document.createElement('input');
            temp.value = texto;
            document.body.appendChild(temp);
            temp.select();
            temp.setSelectionRange(0, 99999);
            try {
                const success = document.execCommand('copy');
                document.body.removeChild(temp);
                return success;
            } catch (e) {
                document.body.removeChild(temp);
                return false;
            }
        }
    }

    // --- Evento para copiar el color ---
    copyBtn.addEventListener('click', async function() {
        const color = colorCodeEl.textContent;
        const ok = await copiarTexto(color);
        if (ok) {
            copyBtn.textContent = '¡Copiado!';
            setTimeout(() => { copyBtn.textContent = 'Copiar Hex'; }, 2000);
        } else {
            alert('No se pudo copiar el código');
        }
    });

    // --- Evento para saludar (llamada POST a la API) ---
    saludarBtn.addEventListener('click', async function() {
        const nombre = nombreInput.value.trim();
        if (nombre === '') {
            alert('Por favor, escribe un nombre');
            return;
        }

        try {
            const response = await fetch('/saludar', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ nombre: nombre })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error al saludar');
            }

            const data = await response.json();
            // Actualizar saludo y color con los datos recibidos
            saludoEl.textContent = data.saludo;
            actualizarColor(data.color);
            nombreInput.value = ''; // limpiar campo

        } catch (error) {
            console.error('Error:', error);
            alert('Hubo un error: ' + error.message);
        }
    });

    // --- Opcional: enviar al presionar Enter en el input ---
    nombreInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            saludarBtn.click();
        }
    });
});
