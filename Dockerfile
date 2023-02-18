FROM python:slim-bullseye

WORKDIR /app

COPY . .

EXPOSE 8080

RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt

CMD python3 /app/run.py
