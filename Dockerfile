FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD python3 -m flask run --host=0.0.0.0