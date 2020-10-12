
# This is:

https://github.com/dgleba/472dkrcollection/tree/master/499d-django


# ref.

https://docs.docker.com/compose/django/


# Installation

- If you have windows OS, install virtualbox and install ubuntu 16 inside it.
- Use ubuntu 16.

```
# cd to a tmp folder
cd tmp
git clone https://github.com/dgleba/472dkrcollection.git
cd 472dkrcollection
cp -a 499d-django/ myshinynewdjangoprojectname
```

- install docker and docker-compose
- Do not install python, or django

# Makefile

Look at the make file for useful commands to speed up using the system.

eg: make clean - this will clean up unneeded containers and such.

make perm   -   to set write permissions on code files.


# commands - for Development

```
docker-compose build

These have already been run against this project..

  docker-compose run --rm djdev django-admin.py startproject djangoproj .

  docker-compose run --rm djdev python manage.py startapp polls
  
  docker-compose run --rm djdev python manage.py startapp contactapp
  
  # This can work with sqlite in development. See production below for use with mysql.

    docker-compose run --rm djdev python manage.py makemigrations blogapp

    docker-compose run --rm djdev python manage.py migrate

    docker-compose run --rm djdev python manage.py createsuperuser


# delete all docker images, containers, volumes, etc for this compose file
# careful..   dkd --rmi all -v

Start a new app..
docker-compose run --rm djdev python manage.py startapp trakberry2

docker-compose exec djdev pip list
docker-compose run --rm djdev pip list

dc up
dc stop
dc restart


visit -    http://10.4.1.228:6461/

admin -   http://10.4.1.228:6461/admin/login/?next=/admin/
  User - root . passw - 123


```

# Pemmissions:

- Docker may run with root or other user.
- To edit files you may have to adjust the permissions.
- use `make perm` to gain permissions to edit/write the files.

# all hosts

in settings.py

```
to get allowed hosts from .env file

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',') if os.getenv('ALLOWED_HOSTS') else []

or
simply..

ALLOWED_HOSTS = ['*']

```

# Production deployment

```
docker-compose -f docker-compose.prod.yml build


docker-compose -f docker-compose.prod.yml run --rm  djprod python manage.py makemigrations

docker-compose -f docker-compose.prod.yml run --rm  djprod python manage.py showmigrations

docker-compose -f docker-compose.prod.yml run --rm  djprod python manage.py migrate

docker-compose -f docker-compose.prod.yml run --rm  djprod python manage.py createsuperuser


no..
  no.. docker-compose run --rm djprod python manage.py collectstatic

yes..
  docker-compose -f docker-compose.prod.yml run --rm  djprod python manage.py collectstatic --noinput


docker-compose -f docker-compose.prod.yml up
docker-compose -f docker-compose.prod.yml stop
docker-compose -f docker-compose.prod.yml restart


# delete containers and data..
# careful...  docker-compose -f docker-compose.prod.yml down -v --remove-orphans



```

# Database commands

examples of commands to import, export, etc are here..

https://github.com/dgleba/482dkrcollection/blob/master/mysqlsimple5/Makefile#L32






# older

# older

# older


I think this may have come from..
     https://github.com/nicholaskajoh/dockerized-django.git

# Dockerized Django

Sample project on how to dockerize your Django project in development and production environments.


## Requirements

- Docker
- Docker Compose

## Development

- Clone project
- Create _.env_ and _.env.secret_ from the example files in the root folder and edit as appropriate
- Run `docker-compose up`
- Visit localhost:8000

## Production

- Follow the first 2 steps outlined above
- Run `docker-compose -f docker-compose.prod.yml up --build -d`
- Run `docker-compose -f docker-compose.prod.yml run web python manage.py migrate`
- Run `docker-compose -f docker-compose.prod.yml run web python manage.py collectstatic --noinput`
- Visit website