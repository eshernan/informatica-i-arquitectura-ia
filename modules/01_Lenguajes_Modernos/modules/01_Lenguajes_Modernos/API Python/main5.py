import random
from string import hexdigits
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def generar_color():
    """Genera un color hexadecimal aleatorio."""
    hex_chars = "".join(random.choices(hexdigits.lower(), k=6))
    return f"#{hex_chars}"


# --- Modelo para el cuerpo de la petición POST ---
class NombreRequest(BaseModel):
    nombre: str


# --- Endpoints de la API ---

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """Sirve la página HTML con un color inicial."""
    color = generar_color()
    return templates.TemplateResponse(
        request=request, name="color5.html", context={"color": color}
    )

@app.get("/color", response_class=JSONResponse)
def get_color():
    """Endpoint público para obtener un color aleatorio en JSON."""
    return {"color": generar_color()}


@app.post("/saludar", response_class=JSONResponse)
def saludar(data: NombreRequest):
    """
    Recibe un nombre y devuelve un saludo personalizado junto con un nuevo color.
    """
    nombre = data.nombre.strip()
    if not nombre:
        raise HTTPException(status_code=400, detail="El nombre no puede estar vacío")
    
    saludo = f"¡Hola {nombre}!"
    nuevo_color = generar_color()
    return {"saludo": saludo, "color": nuevo_color}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main5:app",
        host="0.0.0.0",
        port=8443,
        ssl_keyfile="key.pem",   # si usas HTTPS
        ssl_certfile="cert.pem"
    )
