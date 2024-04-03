[![Actions Status](https://github.com/HugoTheDeveloper/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/HugoTheDeveloper/python-project-52/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4ccf310a748e8bc57f36/test_coverage)](https://codeclimate.com/github/HugoTheDeveloper/task-manager/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/4ccf310a748e8bc57f36/maintainability)](https://codeclimate.com/github/HugoTheDeveloper/task-manager/maintainability)
![Continuous integration](https://github.com/HugoTheDeveloper/task-manager/actions/workflows/continious-integration.yml/badge.svg)

### Showcase
![](https://github.com/HugoTheDeveloper/task-manager/blob/main/showcases/task-manager-showcase.gif)

#### [Check out in action](https://task-manager-s0wy.onrender.com)

### Description

A task management web application built with Python
and Django framework. It allows you to set
tasks, assign executors and change their statuses. Registration and
authentication are required to work with the system.

### Features

* Set tasks;
* Filter the tasks displayed by executors, author, labels and status;
* User authentication and registration;
* Change task status;
* Set multiple tasks labels;
* Assign executors;

### How to install

Clone the project:

    git clone https://github.com/HugoTheDeveloper/task-manager.git && cd task-manager

Create .env file in the root folder and add following variables:

    SECRET_KEY = '{your secret key}' // Django secret key

If you want to use PostgreSQL:
    
    DATABASE_URL = postgresql://{provider}://{user}:{password}@{host}:{port}/{db}

If you choose to use SQLite, do not add DATABASE_URL variable.

For PAAS (Render, Railway, etc):

    HOSTNAME = '{hostname}'

For Rollbar errors tracking:

    ROLLBAR_TOKEN = '{token}'

Then install dependencies and create the tables in the database:
  
    make build

If you want create superuser:

    make create_superuser

## How to use it

Start the gunicorn server by running (UNIX) :

    make start

The server url will be at terminal, for example http://0.0.0.0:8000 or on PAAS server.
___________
Or start the development mode:

    make dev

The server url will be at terminal, for example http://127.0.0.1:8000.
