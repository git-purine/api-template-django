# Start Up

## toc

- django
  - install django
  - install other libraries
  - init django
- i18n
- swagger

## django

### install django

```sh
pipenv install django djangorestframework
```

### install other libraries

```sdh
pipenv install boto3 psycopg2-binary ulid-py

pipenv install --dev autopep8 mypy ptvsd pylint
pipenv install --dev pytest pytest-cov pytest-env pytest-mock
```

### init django

```sh
django-admin startproject api .

mkdir -p apps/helloworld
python manage.py startapp helloworld apps/helloworld
```
