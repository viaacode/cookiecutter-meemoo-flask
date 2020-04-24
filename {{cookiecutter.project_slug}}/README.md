# {{cookiecutter.project_slug}}

## Synopsis

## Prerequisites

* Git
* Docker
* Python 3.6+
* Linux (if you want to run it locally, uwsgi is not available on other platforms.)
* Access to the meemoo PyPi

## Usage

1. Clone this repository with:

    `$ git clone https://github.com/viaacode/{{cookiecutter.project_slug}}.git`

2. Change into the new directory.

### Running locally

1. Start by creating a virtual environment:

    `$ python -m venv ./venv`

2. Activate the virtual environment:

    `$ source ./venv/bin/activate`

3. Install the external modules:

    ```shell
    $ pip install -r requirements.txt \
        --extra-index-url http://do-prd-mvn-01.do.viaa.be:8081/repository/pypi-all/simple \
        --trusted-host do-prd-mvn-01.do.viaa.be && \
      pip install -r requirements-test.txt
    ```

4. Run the tests with:

    `$ python -m pytest -v`

5. Run the application:

   `$ uwsgi -i uwsgi.ini`

The application is now serving requests on `localhost:8080`. Try it with:

    `$ curl -v -X GET localhost:8080/health/live`

### Running using Docker

1. Build the container:

   `$ docker build . -t {{cookiecutter.project_slug}}`

2. Run the container:

   `$ docker run -p 8080:8080 {{cookiecutter.project_slug}}`

You can try the same cURL commands as specified above.