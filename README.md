# django-docker-compose-pipelines-example

## what's inside.
* python3
* Django 1.11

## main commands

### development
* `make install` or `docker-compose build`
*
* `make migrate` or `docker-compose run django python ./manage.py migrate`

* `make runserver` or `docker-compose run -p 8000:8000 django python ./manage.py runserver 0.0.0.0:8000`

### production
* `docker-compose -f docker-compose.yml -f docker-compose-production.yml up -d`

### test
* `make test` or `docker-compose run django py.test -s .`
