from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from pydantic import AnyUrl, constr
import uvicorn
import re

from db import get_short_link, get_long_link
from controller import create_pair_links


webserv = FastAPI()

@webserv.get("/")
async def longlink(long_link: AnyUrl, req: Request):
    create_pair_links(long_link)
    link = f"{req.url.hostname}{req.url.path}{get_short_link(long_link)}"
    # option for UI
    # html = f'''<html><body><a href=>{link}</a></body></html>'''
    # return HTMLResponse(content=html)
    return link


@webserv.get("/{short_link}")
async def redirect(short_link):                 # constr(regex=r"\b[\d|a-f]{5}\b"
    if re.match(r"\b[\d|a-f]{5}\b", short_link):
        long_link = get_long_link(short_link)
        return RedirectResponse(long_link)
    return "Incorrect short link"


if __name__ == "__main__":
    uvicorn.run("webserv:webserv", host="127.0.0.1", port=80, log_level="info")
    
