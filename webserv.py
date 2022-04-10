from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import AnyUrl
import re

from db import get_short_link, get_long_link
from controller import create_pair_links


webserv = FastAPI()

@webserv.get("/")
async def longlink(url: AnyUrl, req: Request):
    create_pair_links(url)
    link = f"{req.url.hostname}{req.url.path}{get_short_link(url)}"
    # option for UI
    # html = f'''<html><body><a href=>{link}</a></body></html>'''
    # return HTMLResponse(content=html)
    return link


@webserv.get("/{short_link}")
async def redirect(short_link):
    if re.match(r"\b[\d|a-f]{5}\b", short_link):
        long_link = get_long_link(short_link)
        if long_link:
            return RedirectResponse(long_link)
    return {"err": "Incorrect short link"}
