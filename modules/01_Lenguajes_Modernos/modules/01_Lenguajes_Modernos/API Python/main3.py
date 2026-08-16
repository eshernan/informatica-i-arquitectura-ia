import random
from string import hexdigits

from fastapi import FastAPI, Request
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
    }
    return templates.TemplateResponse(
        request=request, name="color.html", context=context
    )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main3:app",
        host="0.0.0.0",           # Escucha en todas las interfaces (para pruebas)
        port=8443,                # Puerto para HTTPS (puedes cambiarlo)
        ssl_keyfile="key.pem",    # Ruta a tu clave privada
        ssl_certfile="cert.pem",  # Ruta a tu certificado
    )
