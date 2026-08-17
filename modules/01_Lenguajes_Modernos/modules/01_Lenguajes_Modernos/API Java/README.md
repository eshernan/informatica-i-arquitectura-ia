# Cómo Servir un Sitio Web con Spring Boot Usando HTML y Thymeleaf

Al final de esta guía, podrás servir sitios web dinámicos desde endpoints de Spring Boot utilizando plantillas Thymeleaf con CSS y JavaScript. Aprovechando las clases `@Controller`, `@ResponseBody` y `@RestController` de Spring Boot, usarás Spring Boot como un framework web tradicional de Java.

Comenzarás devolviendo HTML básico desde tus endpoints, luego agregarás plantillas Thymeleaf para contenido dinámico y, finalmente, crearás un sitio web completo con archivos CSS y JavaScript externos para copiar códigos de color hexadecimales.

Para continuar, debes sentirte cómodo con las funciones de Java y tener un conocimiento básico de HTML y CSS. La experiencia con Spring Boot es útil, pero no es necesaria.

---

## Prerrequisitos

Antes de comenzar a construir tu aplicación Spring Boot que sirve HTML, necesitarás configurar tu entorno de desarrollo con los paquetes requeridos. Instalarás Spring Boot junto con sus dependencias estándar, incluyendo el servidor Tomcat que necesitas para ejecutar tu aplicación.

### 1. Instalar JDK 25+ (Requerido)

Spring Boot 3.x requiere **Java 25** o superior. Verifica tu versión:

```bash
java -version
```

Si no tienes JDK 25, instálalo:

Ubuntu 22 / Linux:

```bash
sudo apt update
sudo apt install openjdk-25-jdk -y
```

Windows:
Descarga e instala desde Oracle JDK o OpenJDK.

### 2. Instalar Eclipse IDE (con Spring Tools 4)
Descarga Eclipse IDE for Enterprise Java and Web Developers desde eclipse.org.

Al abrir Eclipse, ve a Help → Eclipse Marketplace y busca "Spring Tools 4". Instálalo y reinicia Eclipse.

Alternativamente, usa Spring Tool Suite (STS) que ya viene con todo preinstalado.

### 3. Crear el Proyecto Spring Boot
1. En Eclipse, ve a File → New → Spring Starter Project.

2. Completa los campos:

Name: ColorApiJava

Type: Maven

Group: com.example

Artifact: ColorApiJava

Package: com.example.colorapi

Packaging: Jar

Java Version: 25

Language: Java

3. Haz clic en Next.

4. Selecciona las dependencias:

Spring Web (spring-boot-starter-web)

Thymeleaf (spring-boot-starter-thymeleaf)

Spring Boot DevTools (opcional)

5. Haz clic en Finish. Eclipse descargará las dependencias y generará el proyecto.


###Paso 1: Devolver HTML básico a través de un endpoint
Spring Boot, al igual que FastAPI, permite devolver contenido HTML directamente desde un controlador.

Crea un nuevo archivo ColorController.java en el paquete com.example.colorapi:

```Java
package com.example.colorapi;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class ColorController {

    @GetMapping("/")
    @ResponseBody
    public String home() {
        return """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Home</title>
                </head>
                <body>
                    <h1>Welcome to Spring Boot!</h1>
                </body>
                </html>
                """;
    }
}
```
Ejecuta la aplicación:

Haz clic derecho en el proyecto → Run As → Spring Boot App.

Visita http://localhost:8080/ (puerto por defecto).

Verás "Welcome to Spring Boot!".

### Paso 2: Mejorar con Thymeleaf para contenido dinámico

Thymeleaf es el motor de plantillas recomendado para Spring Boot. Vamos a crear un generador de colores aleatorios.

#### 2.1. Crear la plantilla color.html

En src/main/resources/templates/, crea un archivo color.html:

~~~html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Random Color Generator</title>
    <style>
        body {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: black;
            color: white;
            font-size: 120px;
            font-family: monospace;
        }
    </style>
</head>
<body>
    <div id="color-code" th:text="${color}">#000000</div>
    <style>
        body {
            background-color: [[${color}]];
        }
	</style>
</body>
</html>
```
#### 2.2. Modificar el Controlador

Actualiza ColorController.java:

```java
package com.example.colorapi;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.Random;

@Controller
public class ColorController {

    private final Random random = new Random();

    private String generarColor() {
        return String.format("#%06x", random.nextInt(0xFFFFFF + 1));
    }

    @GetMapping("/")
    public String home(Model model) {
        String color = generarColor();
        model.addAttribute("color", color);
        return "color";  // Busca color.html en templates/
    }
}
```

Recarga la página para ver diferentes colores.

### Paso 3: Estructura completa con archivos estáticos y JavaScript
Para crear una experiencia más completa, separaremos el CSS y el JavaScript en archivos externos y añadiremos un botón para copiar el color.

#### 3.1. Crear la carpeta static
Dentro de src/main/resources/, crea la carpeta static/. Allí guardarás style.css y script.js.

#### 3.2. Plantilla base base.html (reutilizable)
En src/main/resources/templates/, crea base.html:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Random Color Generator</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <div th:replace="~{::content}"></div>
    <script src="/script.js"></script>
</body>
</html>
```

#### 3.3. Plantilla color.html extendiendo base.html

Modifica color.html:

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>Random Color Generator</title>
    <link rel="stylesheet" href="/style.css">
</head>
<body>
    <div id="color-code" th:text="${color}">#000000</div>
    <button id="copy-button">Copiar Hex</button>
    <div id="saludo"></div>
    <div>
        <input type="text" id="nombre-input" placeholder="Escribe tu nombre" required>
        <button id="saludar-button">Saludar</button>
    </div>

    <script src="/script.js"></script>
</body>
</html>
```

Nota: Las rutas a CSS y JS son /style.css y /script.js, no /static/... porque Spring Boot sirve automáticamente desde static/ en la raíz del contexto.

#### 3.4. Archivo style.css

En src/main/resources/static/style.css:

```css
body {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    font-family: monospace;
    transition: background-color 0.3s ease;
    background-color: black;
}

#color-code {
    font-size: 120px;
    margin-bottom: 20px;
}

#saludo {
    font-size: 60px;
    margin: 20px;
    min-height: 70px;
}

button, input {
    font-size: 30px;
    padding: 10px 20px;
    margin: 10px;
    border-radius: 8px;
    border: none;
}

button {
    background-color: rgba(255,255,255,0.2);
    color: white;
    cursor: pointer;
}

button:hover {
    background-color: rgba(255,255,255,0.4);
}

input {
    background-color: rgba(255,255,255,0.3);
    color: white;
}

input::placeholder {
    color: rgba(255,255,255,0.7);
}
```

#### 3.5. Archivo script.js

En src/main/resources/static/script.js:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const colorCodeEl = document.getElementById('color-code');
    const saludoEl = document.getElementById('saludo');
    const copyBtn = document.getElementById('copy-button');
    const nombreInput = document.getElementById('nombre-input');
    const saludarBtn = document.getElementById('saludar-button');

    function actualizarColor(color) {
        document.body.style.backgroundColor = color;
        colorCodeEl.textContent = color;
    }

    // Copiar con fallback (para HTTP/HTTPS local)
    async function copiarTexto(texto) {
        try {
            await navigator.clipboard.writeText(texto);
            return true;
        } catch (err) {
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

    saludarBtn.addEventListener('click', async function() {
        const nombre = nombreInput.value.trim();
        if (nombre === '') {
            alert('Por favor, escribe un nombre');
            return;
        }

        try {
			const formData = new FormData();
			formData.append('nombre', nombre);

            const response = await fetch('/saludar', {
                method: 'POST',
				body: formData
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error al saludar');
            }

            const data = await response.json();
            saludoEl.textContent = data.saludo;
            actualizarColor(data.color);
            nombreInput.value = '';
        } catch (error) {
            alert('Hubo un error: ' + error.message);
        }
    });

    nombreInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            saludarBtn.click();
        }
    });
});
```
#### 3.6. Archivo ColorControler.java

En /src/main/java/com/example/colorapi/ColorController.java:

```java
package com.example.colorapi;

import java.util.Random;
import java.util.Map;
import java.util.HashMap;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class ColorController {

    private String generarColorHex() {
        Random rand = new Random();
        int r = rand.nextInt(256);
        int g = rand.nextInt(256);
        int b = rand.nextInt(256);
        return String.format("#%02x%02x%02x", r, g, b);
    }

    // --- Página principal con el generador de colores (GET) ---
    @GetMapping("/")
    public String home(Model model) {
        String color = generarColorHex();
        model.addAttribute("color", color);
        return "color"; // corresponde a templates/color.html
    }

    // --- Endpoint para obtener solo el color en JSON (GET) ---
    @GetMapping("/color")
    @ResponseBody
    public Map<String, String> getColor() {
        Map<String, String> response = new HashMap<>();
        response.put("color", generarColorHex());
        return response;
    }

    // --- Endpoint para saludar (POST) ---
    @PostMapping("/saludar")
    @ResponseBody
    public Map<String, String> saludar(@RequestParam String nombre) {
        if (nombre == null || nombre.trim().isEmpty()) {
            throw new IllegalArgumentException("El nombre no puede estar vacío");
        }
        Map<String, String> response = new HashMap<>();
        response.put("saludo", "¡Hola " + nombre.trim() + "!");
        response.put("color", generarColorHex());
        return response;
    }
}
```


### Paso 4: Desplegar en HTTPS con certificados SSL

Para que el botón "Copiar" funcione en navegadores modernos, necesitamos HTTPS.

#### 4.1. Generar el almacén de claves (keystore)

Si tienes cert.pem y key.pem, conviértelos a PKCS12:

```bash
openssl pkcs12 -export -in cert.pem -inkey key.pem -out keystore.p12 -name tomcat -password pass:estudiantes
```

Coloca keystore.p12 en src/main/resources/.

Si NO  tienes cert.pem y key.pem, vamos a generar un certificado nuevo PKCS12:

 ```bash
 keytool -genkey -alias tomcat -storetype PKCS12 -keyalg RSA -keysize 2048 -keystore keystore.p12 -validity 365 -dname "CN=localhost, OU=, O=, L=, ST=, C="
 ```
 
 Ponerle una clave y coloca keystore.p12 en src/main/resources/.

#### 4.2. Configurar application.properties

En src/main/resources/application.properties:

```properties
spring.application.name=ColorApiJava
server.port=8443
server.ssl.key-store=classpath:keystore.p12
server.ssl.key-store-password=estudiantes
server.ssl.key-store-type=PKCS12
server.ssl.key-alias=tomcat
```
#### 4.3. Ejecutar con HTTPS

La aplicación ahora estará en https://localhost:8443/.


### Paso 5: Crear una API REST con endpoints GET y POST

Ahora convertimos la aplicación en una API consumible que no lea del formulario si no responda el POST a traves de una JSON.

#### 5.1. Modelo NombreRequest

Crea NombreRequest.java:

```java
package com.example.colorapi;

public class NombreRequest {
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
}
```

#### 5.2. Controlador con endpoints REST

Actualiza ColorController.java con los nuevos endpoints:

```java 
package com.example.colorapi;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;
import java.util.Random;

@Controller
public class ColorController {

    private final Random random = new Random();

    private String generarColor() {
        return String.format("#%06x", random.nextInt(0xFFFFFF + 1));
    }

    // GET / → página HTML
    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("color", generarColor());
        return "color";
    }

    // GET /color → JSON con color
    @GetMapping("/color")
    @ResponseBody
    public Map<String, String> getColor() {
        Map<String, String> response = new HashMap<>();
        response.put("color", generarColor());
        return response;
    }

    // POST /saludar → recibe JSON y devuelve JSON
    @PostMapping("/saludar")
    @ResponseBody
    public ResponseEntity<Map<String, String>> saludar(@RequestBody NombreRequest request) {
        String nombre = request.getNombre();

        if (nombre == null || nombre.trim().isEmpty()) {
            Map<String, String> error = new HashMap<>();
            error.put("detail", "El nombre no puede estar vacío");
            return ResponseEntity.badRequest().body(error);
        }

        Map<String, String> response = new HashMap<>();
        response.put("saludo", "¡Hola " + nombre.trim() + "!");
        response.put("color", generarColor());
        return ResponseEntity.ok(response);
    }
}
```

#### 5.3. Modifica el javascript para que pueda enviar peticiones POST por Json y no por Form.

en el archivo /resources/script.js modifica el metodo del boton saludar, para que no envie los datos por FORM si no JSON, de la siguiente manera:

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const colorCodeEl = document.getElementById('color-code');
    const saludoEl = document.getElementById('saludo');
    const copyBtn = document.getElementById('copy-button');
    const nombreInput = document.getElementById('nombre-input');
    const saludarBtn = document.getElementById('saludar-button');

    function actualizarColor(color) {
        document.body.style.backgroundColor = color;
        colorCodeEl.textContent = color;
    }

    // Copiar con fallback
    async function copiarTexto(texto) {
        try {
            await navigator.clipboard.writeText(texto);
            return true;
        } catch (err) {
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

    saludarBtn.addEventListener('click', async function() {
        const nombre = nombreInput.value.trim();
        if (nombre === '') {
            alert('Por favor, escribe un nombre');
            return;
        }

		try {
				//const formData = new FormData();
				//formData.append('nombre', nombre);

		           const response = await fetch('/saludar', {
		            method: 'POST',
					headers: { 'Content-Type': 'application/json' },
					body: JSON.stringify({ nombre: nombre })
					  //body: formData
		           });


            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error al saludar');
            }

            const data = await response.json();
            saludoEl.textContent = data.saludo;
            actualizarColor(data.color);
            nombreInput.value = '';
        } catch (error) {
            alert('Hubo un error: ' + error.message);
        }
    });

    nombreInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            saludarBtn.click();
        }
    });
});
```

#### 5.4. Manejo global de errores (opcional)


Crea GlobalExceptionHandler.java para capturar excepciones no controladas:

```java
package com.example.colorapi;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.util.HashMap;
import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(Exception.class)
    public ResponseEntity<Map<String, String>> handleGenericException(Exception e) {
        Map<String, String> error = new HashMap<>();
        error.put("detail", "Error interno: " + e.getMessage());
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(error);
    }
}
```

### Paso 6: Consumir la API desde el Frontend (fetch)

El script.js ya usa fetch para enviar peticiones POST al endpoint /saludar y actualizar el color y el saludo sin recargar la página.

La estructura final del proyecto debe ser:

```text
ColorApiJava/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/example/colorapi/
│   │   │       ├── ColorApiJavaApplication.java
│   │   │       ├── ColorController.java
│   │   │       ├── NombreRequest.java
│   │   │       └── GlobalExceptionHandler.java
│   │   ├── resources/
│   │   │   ├── static/
│   │   │   │   ├── style.css
│   │   │   │   └── script.js
│   │   │   ├── templates/
│   │   │   │   └── color.html
│   │   │   └── application.properties
│   └── test/
└── pom.xml
```

### Paso 7: Probar con Postman

GET /color
URL: https://localhost:8443/color

Método: GET

Respuesta:

```json
{
    "color": "#a1b2c3"
}
```

POST /saludar
URL: https://localhost:8443/saludar

Método: POST

Headers: Content-Type: application/json

Body (raw JSON):

```json
{
    "nombre": "Ana"
}
```

Respuesta

```json
{
    "saludo": "¡Hola Ana!",
    "color": "#d4e5f6"
}
```

### Paso 8: Desplegar en Ubuntu 22

#### 8.1. Generar el JAR

Desde Eclipse: 

Spring Boot puede empaquetarse como un archivo JAR ejecutable. En Eclipse:

Haz clic derecho sobre el proyecto → Run As → Maven build...

En Goals escribe: clean package

Marca Skip Tests si quieres acelerar (opcional).

Haz clic en Run.

Esto generará un archivo .jar en la carpeta target/ del proyecto, con un nombre similar a ColorApiJava-0.0.1-SNAPSHOT.jar.

Desde Consola:

Alternativa en consola (desde la raíz del proyecto):

```bash
mvn clean package
```
El JAR se genera en target/ColorApiJava-0.0.1-SNAPSHOT.jar.

#### 8.2. Copiar el JAR al servidor

```bash
scp target/ColorApiJava-0.0.1-SNAPSHOT.jar usuario@tu-ip:/ruta/destino/
```

#### 8.3. Instalar Java en el servidor
```bash
sudo apt update
sudo apt install openjdk-25-jre-headless -y
```

#### 8.4. Ejecutar la aplicación
```bash
java -jar ColorApiJava-0.0.1-SNAPSHOT.jar
```

Para ejecutar en segundo plano:

```bash
nohup java -jar ColorApiJava-0.0.1-SNAPSHOT.jar > app.log 2>&1 &
```

Para el proceso en segundo plano:

```bash
kill -9 PID
```
por ejemplo 

```bash
kill -9 7937
```


#### 8.5. Abrir el puerto en el firewall
```bash
sudo ufw allow 8443/tcp
```

### Resumen de Endpoints

| Método | URL | Descripción | Cuerpo (POST) | Respuesta |
| GET | / | Página HTML | - | HTML |
| GET | /color | Color aleatorio en JSON | - | `{"color":"#a1b2c3"}` |
| POST | /saludar | Enviar nombre, recibir saludo + color | `{"nombre":"Ana"}` | `{"saludo":"¡Hola Ana!","color":"#d4e5f6"}` |


###Solución de Problemas Comunes

-Error al importar spring-boot-starter-webmvc
Usa spring-boot-starter-web en lugar de webmvc.

-El CSS/JS no se cargan (404)
En color.html, las rutas deben ser /style.css y /script.js (sin /static/).

Asegúrate de que los archivos estén en src/main/resources/static/.

-"Hubo un error: Error al saludar"
Revisa la consola del navegador (F12) para ver el error exacto.

Acepta el certificado autofirmado visitando primero la página.

Verifica que el servidor esté corriendo y que el puerto sea accesible.

-El puerto 8443 ya está en uso
Cambia el puerto en application.properties o mata el proceso:

```bash
sudo lsof -i :8443
sudo kill -9 <PID>
```
