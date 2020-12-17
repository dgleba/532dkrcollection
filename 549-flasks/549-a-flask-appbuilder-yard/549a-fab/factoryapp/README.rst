FactoryApp
----------

Simple example to show how to use a factory setup.

Create an Admin user and insert test data::

    $ python testdata.py

Run it::

    $ export FLASK_APP="app:create_app('config')"
    $ flask fab create-admin
    $ flask run

Try it. Open a browser to http://localhost:5000.

Using an alternate config::

    $ export FLASK_APP="app:create_app('config2')"
    $ flask fab create-admin
    $ flask run


=================================================

    docker-compose run --rm flaskdev bash -c '  python testdata.py'

    docker-compose run --rm flaskdev bash -c ' export FLASK_APP="app:create_app('config')"; flask fab create-admin '

    docker-compose exec flaskdev bash -c ' export FLASK_APP=app; flask run --host 0.0.0.0'



no:

    docker-compose run --rm flaskdev bash -c ' export FLASK_APP="app:create_app('config')"; flask run --host 0.0.0.0'
        * Serving Flask app "app:create_app(config)"
        * Environment: production
        WARNING: This is a development server. Do not use it in a production deployment.
        Use a production WSGI server instead.
        * Debug mode: off
        Usage: flask run [OPTIONS]
            Error: Could not parse the arguments in "create_app(config)".


