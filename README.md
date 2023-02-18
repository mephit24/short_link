API service of short links.  

For get short link send get-request like this: "http://address_of_service/?url=https://someurl.com". 
Use url "http://address_of_service/api/" to get API response, which is list of links. 

Short link sending on service will be redirect to you address: http://address_of_service/shortlink.   

You can make custom short link (you can use no more than 50 chars), using parametr "custom". Example: "http://address_of_service/?url=https://someurl.com&custom=mylink".

## For start application:

* Clone application from Github:
  ```bash
  git clone https://github.com/mephit24/short_link.git
  ```
  Or download it:
  https://github.com/mephit24/short_link/archive/refs/heads/main.zip

* Go to app directory:
  ```bash
  cd /path/to/app
* Run only for first time:
  ```bash
  python3 -m pip install -r requirements.txt
* Run:
  ```bash
  uvicorn webserv:webserv --reload --port=8080
  ```
  *You can see manual:* https://www.uvicorn.org/deployment/#running-from-the-command-line
* Open url http://127.0.0.1:8080 in your internet browser.

## For start application in Docker:

* Install Docker:  
  + https://docs.docker.com/engine/install  

* Run:
  ```bash
  docker run -d -p 8080:8080 mephit/short_link
* Open url http://127.0.0.1:8080 in your internet browser.
