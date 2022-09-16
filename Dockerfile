FROM python:3.9

ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . /code/

RUN pip install --no-cache-dir --upgrade -r requirements.txt

