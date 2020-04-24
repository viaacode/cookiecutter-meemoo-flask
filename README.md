# Cookiecutter meemoo flask

## Synopsis

A cookiecutter project that will create a flask meemooo app aiming to generate the bulk
of the boilerplate code taking into account the best practices.

## Prerequisites

- Git
- Python 3.6+

## Usage

Install Cookiecutter if you haven't already:

   ```shell
   $ pip3 install cookiecutter>=1.7.2
   ```

Change into the directory in which you want to create a project.

Create a project:

   ```shell
   `$ cookiecutter https://github.com/viaacode/cookiecutter-meemoo-flask.git
   ```

Instead, you can also manually clone the Cookiecutter project:

   ```shell
   `$ git clone https://github.com/viaacode/cookiecutter-meemoo-flask.git
   ```

Create the project:

   ```shell
   `$ cookiecutter /cookiecutter-repo-folder
   ```

You will be prompted to fill in some variables:

   ```shell
   project_name [Python Project]: Flask test
   project_slug [flask-test]: 
   organization [meemoo]: 
   python_version [3.6]: 
   Select dockerfile_stages:
   1 - single
   2 - multi
   Choose from 1, 2 [1]: 
   Select open_source_license:
   1 - MIT license
   2 - BSD license
   3 - ISC license
   4 - Apache Software License 2.0
   5 - GNU General Public License v3
   6 - Not open source
   Choose from 1, 2, 3, 4, 5, 6 [1]: 
   ```

Change into the project and look around:

   ```shell
   $ cd flask-test/
   $ ls -l
   ```

Be sure to check out the generated `README.md` to quickly setup/test the created project (see: Usage).

If you have `Docker` installed you can quickly get something started by using the accompanied `Makefile`:

   ```shell
   make -f Makefile-docker build && make -f Makefile-docker app
   ```

In a different terminal, execute:

   ```shell
   $ curl -v -X GET localhost:8080/health/live
   ```