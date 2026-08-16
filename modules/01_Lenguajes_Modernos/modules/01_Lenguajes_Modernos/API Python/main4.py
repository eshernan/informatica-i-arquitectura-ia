import random
from string import hexdigits
from fastapi import FastAPI, Request, Form          # ← importamos Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    hex_chars = "".join(random.choices(hexdigits.lower(), k=6))
    hex_color = f"#{hex_chars}"
    context = {
        "color": hex_color,
        "saludo": None,          # ← sin saludo en GET
    }
    return templates.TemplateResponse(
        request=request, name="color2.html", context=context
    )


@app.post("/", response_class=HTMLResponse)   # ← nueva ruta POST
def saludar(request: Request, nombre: str = Form(...)):
    hex_chars = "".join(random.choices(hexdigits.lower(), k=6))
    hex_color = f"#{hex_chars}"
    saludo = f"¡Hola {nombre}!"                # ← saludo personalizado
    context = {
        "color": hex_color,
        "saludo": saludo,
    }
    return templates.TemplateResponse(
        request=request, name="color2.html", context=context
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main4:app",
        host="0.0.0.0",
        port=8443,
        ssl_keyfile="key.pem",   # si usas HTTPS
        ssl_certfile="cert.pem"
    )

    