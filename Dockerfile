FROM python:3.10.2-alpine3.15

RUN apk update && apk add --virtual build-deps \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev
WORKDIR /app

ADD requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ADD . /app/
