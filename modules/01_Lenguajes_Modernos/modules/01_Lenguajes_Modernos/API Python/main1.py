import random
from string import hexdigits

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from jinja2 import Template

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    hex_chars = "".join(random.choices(hexdigits.lower(), k=6))
    hex_color = f"#{hex_chars}"
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Random Color Generator</title>
        <style>
            body {
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background-color: {{ color }};
                color: white;
                font-size: 120px;
                font-family: monospace;
            }
        </style>
    </head>
    <body>
        <div id="color-code">{{ color }}</div>
    </body>
    </html>
    """

    html_content = Template(html_template)
    website = html_content.render(color=hex_color)

    return website
