import uvicorn

if __name__ == "__main__":
    uvicorn.run("webserv:webserv", host="127.0.0.1", port=8080, log_level="info")
    