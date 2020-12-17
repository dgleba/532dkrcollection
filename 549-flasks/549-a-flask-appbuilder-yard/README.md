#

https://flask-appbuilder.readthedocs.io/en/latest/cli.html


dc build

    docker-compose run --rm flaskdev bash -c 'flask fab create-app'

    docker-compose run --rm flaskdev bash -c 'cd appa; flask fab create-admin'

    docker-compose run --rm flaskdev bash -c 'cd appa; flask run --host 0.0.0.0'

    docker-compose run --rm flaskdev bash -c 'export FLASK_APP=app/__init__.py; flask run --host 0.0.0.0'
    
    docker-compose run --rm flaskdev bash -c 'export FLASK_APP=app/__init__.py; flask fab create-admin'


    docker-compose run --rm flaskdev bash -c 'flask fab create-admin'


