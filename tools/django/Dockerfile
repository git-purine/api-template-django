FROM python:3.7-alpine

RUN apk add --update --no-cache \
  linux-headers \
  g++ \
  python3-dev \
  postgresql-dev

WORKDIR /django

# install
RUN pip install --no-cache-dir \
  pipenv

COPY ./Pipfile ./
COPY ./Pipfile.lock ./
RUN pipenv install --system -d

EXPOSE 8000
