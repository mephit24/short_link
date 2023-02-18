from pydantic import AnyUrl
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

from db import get_short_link, get_long_link
from controller import create_pair_links


webserv = FastAPI()
html_templates = Jinja2Templates(directory='html_templates')

@webserv.get("/check")
async def check():
    return "Short_link version 0.1"

@webserv.get("/")
async def longlink(url: AnyUrl, req: Request, custom: str = None):
    err = False if create_pair_links(url, custom=custom) else True
    return html_templates.TemplateResponse('main.html', {'request': req,
                                                         'links': get_short_link(url),
                                                         'long_link': url,
                                                         'err': err})

@webserv.get("/api/")
async def longlink_api(url: AnyUrl, req: Request, custom: str = None):
    api_obj = {url: ['/'.join((f"{req.url.hostname}:{req.url.port}", link)) for link in get_short_link(url)]}
    if create_pair_links(url, custom=custom):
        return api_obj
    return {"err": "Link already exist"}, api_obj

@webserv.get("/{short_link}")
async def redirect(short_link):
    long_link = get_long_link(short_link)
    if long_link:
        return RedirectResponse(long_link)
    return {"err": "Incorrect short link"}
