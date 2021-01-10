#

https://flask-appbuilder.readthedocs.io/en/latest/cli.html





See demo1/readme.rst



more example commands..



dc build

    docker-compose run --rm flaskdev bash -c 'flask fab create-app'


Later, i moved the app up a folder from appa to the parent. So `cd appa;` should not be needed.

    docker-compose run --rm flaskdev bash -c 'cd appa; flask fab create-admin'

    docker-compose run --rm flaskdev bash -c 'cd appa; flask run --host 0.0.0.0'


    docker-compose run --rm flaskdev bash -c 'export FLASK_APP=app/__init__.py; flask run --host 0.0.0.0'
    

create admin user:

    docker-compose run --rm flaskdev bash -c 'export FLASK_APP=app/__init__.py; flask fab create-admin'


    docker-compose run --rm flaskdev bash -c 'flask fab create-admin'

to run:

    dc up



upgrade pip due to error:


dc run --rm flaskdev bash -c 'pip install --upgrade setuptools pip'


pip

dc run --rm flaskdev bash -c 'pip freeze'

