FROM python:3.7-slim-stretch

WORKDIR /usr/

COPY app app
COPY models models

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV FLASK_APP=app/flask_app.py

CMD flask run --host=0.0.0.0 

