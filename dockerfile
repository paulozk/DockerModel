FROM python:3

WORKDIR /usr/src

COPY models models
COPY src src
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD python src/model_predict.py
