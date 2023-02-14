FROM python:slim-bullseye

WORKDIR /app

COPY . .

EXPOSE 8080

RUN python3 -m pip install -r requirements.txt

CMD python3 /app/run.py
