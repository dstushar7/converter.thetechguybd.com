from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import convert as doConvert 

app = FastAPI()

# Mount the "static" directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Tell FastAPI where your templates are located
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Renders the index.html template (in templates/index.html).
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert")
async def convert_text(request: Request):
    """
    Reads JSON from the request body, checks 'type' and 'text' keys,
    and returns converted text as JSON.
    """
    data = await request.json()
    conversion_type = int(data["type"])
    text = data["text"]

    # Perform the conversion based on the 'type'
    if conversion_type == 1:
        result = unicode_to_bijoy(text)
    else:
        result = bijoy_to_unicode(text)

    return JSONResponse({"result": result})

def unicode_to_bijoy(text: str) -> str:
    """
    Example function to convert from Unicode to Bijoy using your custom module.
    """
    converter = doConvert.Unicode()  # Adjust to match your actual class or function
    return converter.convertUnicodeToBijoy(text)

def bijoy_to_unicode(text: str) -> str:
    """
    Placeholder function for the opposite conversion (Bijoy to Unicode).
    """
    return text

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
