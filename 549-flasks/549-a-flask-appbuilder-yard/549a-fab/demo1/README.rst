Quick How to Example
--------------------

Simple contacts application.

Insert test data::

    $ python testdata.py

Run it::

    $ export FLASK_APP=app/__init__.py
    $ flask fab create-admin
    $ flask run


=================================================

    docker-compose run --rm flaskdev bash -c '  python testdata.py'

    docker-compose run --rm flaskdev bash -c ' export FLASK_APP=app/__init__.py; flask fab create-admin '

    # this didn't add field..
    docker-compose run --rm flaskdev bash -c ' export FLASK_APP=app/__init__.py; flask fab create-db '

    docker-compose exec flaskdev bash -c ' export FLASK_APP=app; flask run --host 0.0.0.0'


