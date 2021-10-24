# pull official base image
FROM python:3.9-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV SECRET_KEY "django-insecure-jc)3ymo4411324+g_=!wrgh4n_hb5-h4xuf-5ssgw*%fqm5j-^"

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies

COPY ./boilerplate/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD cd ./boilerplate && gunicorn boilerplate.wsgi:application --bind 0.0.0.0:$PORT