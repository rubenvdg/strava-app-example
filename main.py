from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory="templates")


@app.get("/auth/", response_class=HTMLResponse)
async def do_auth(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})


@app.get("/redirect/", response_class=HTMLResponse)
async def read_item(request: Request, state: str = "", code: str = "", scope: str = ""):
    return templates.TemplateResponse("redirect.html", {"request": request, "code": code})
