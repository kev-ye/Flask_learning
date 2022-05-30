# flask_learning

## Virtualize

```shell
python3 -m venv venv # set virtualize environment
. venv/bin/activate # run virtualize environment
```

## Installation

```shell
pip3 install -e . # packages installation
```

## Test

```shell
pip3 install pytest coverage # tools installation

pytest # basic run
coverage run -m pytest # coverage
coverage report # report
coverage html # html report
```

## Run

```shell
export FLASK_APP=flaskr # set flask app
export FLASK_ENV=development # set development mode

flask init-db # initialize database
flask run # run flask app
```

## Deploy step

```shell
pip install wheel # tools installation, python standard release file is .whl
python setup.py bdist_wheel # create dist
# --> create venv environment first
pip install flaskr-1.0.0-py3-none-any.whl # installation

export FLASK_APP=flaskr # set flask app
flask init-db # initialize database

python -c 'import os; print(os.urandom(16))' # create a secure secret key
echo 'SECRET_KEY' > venv/var/flaskr-instance/config.py # secret_key file, read by app.config.from_pyfile

pip install waitress # product server example with waitress
waitress-serve --call 'flaskr:create_app' # deploy with waitress
```