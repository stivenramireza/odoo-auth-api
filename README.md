# Odoo Auth API

User management and authentication API using Odoo 14 external web service.

<p align="center">
<img src="https://odoo-development.readthedocs.io/en/latest/_images/log-in-as-superuser-odoo-12.png">
</p>

## Run API in development mode

    $ pip install -r requirements.txt
    $ uvicorn src.main:app --reload

## Run API in production mode

    $ docker build -t odoo-auth:latest .
	$ docker-compose up -d
