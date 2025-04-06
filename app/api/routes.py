from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from services.convert_util import unicode_to_bijoy, bijoy_to_unicode


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Renders the index.html template (in templates/index.html).
    """
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/convert")
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
