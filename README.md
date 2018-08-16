# scoping-tmv

Scoping-tmv is a web application for working with literature. It assists in doing systematic reviews, and has some tools to run topic models on article abstracts.

It was developed to work with **Python 3** and **Django 2.1**. It relies on a PostgreSQL database.

## Quick-start

The following instructions assume installation on Ubuntu (18). Consult the internet for setting up PostgreSQL and Python/pip in other environments.

### Setting up PostgreSQL

If you do not have PostgreSQL installed already, install it. At time of writing, the latest release was PostgreSQL 10. This version is assumed. We also need postgis to handle geographical data

```
sudo apt update
sudo apt install postgresql postgresql-contrib postgis
```

Log on as the postgres user and start PostgreSQL
```
sudo -u postgres  -i
psql
```

Create a new user for this app (call it whatever you like), use a secure password, in single quotes:
```
CREATE USER scoper WITH PASSWORD 'secure_password';
```

Create a database for the app, use whatever name you like:
```
CREATE DATABASE scoping_tmv OWNER scoper;
```

Quit PostgreSQL and log out of the postgres user role

```
\q
exit
```

### Setting up Celery
We use celery to execute computation-heavy tasks in the background.
To do this we need to install the *message broker* RabbitMQ

```
sudo apt-get install rabbitmq-server
sudo systemctl enable rabbitmq-server
sudo systemctl start rabbitmq-server
```

To start celery, run

```
celery -A config worker --loglevel=info
```

##### Production environment for celery

Install supervisor
```
sudo apt-get install supervisor
```
Create a configuration file in `/etc/supervisor/conf.d/scoping-tmv-celery.conf`:
use paths to the production version of the site, it's virtual environment
```
[program:mysite-celery]
command=/home/mysite/bin/celery worker -A mysite --loglevel=INFO
directory=/home/mysite/mysite
user=nobody
numprocs=1
stdout_logfile=/home/mysite/logs/celery.log
stderr_logfile=/home/mysite/logs/celery.log
autostart=true
autorestart=true
startsecs=10

; Need to wait for currently executing tasks to finish at shutdown.
; Increase this if you have very long running tasks.
stopwaitsecs = 600

stopasgroup=true

; Set Celery priority higher than default (999)
; so, if rabbitmq is supervised, it will start first.
priority=1000
```


### Setting up scoping-tmv

Operating in a virtual environment is **highly** recommended

```
pip3 install --user virtualenvironment

virtualenvironment -p python3 venv
```

Once in the environment (or out of it at your own peril), install dependencies

```
pip install -Ur requirements/local.txt
```

generate a `.env` file containing a new secret key (keep this secret!) and your database settings.

```
python env_gen.py
```

Now you're ready to run a local server

```
python manage.py runserver
```

in a production environment:

Install Apache
```
sudo apt-get install apache2
```


Start the server with production settings. It's best to do this in a real server with `mod_wsgi`. This is not covered here.

```
python manage.py runserver --settings=config.settings.production
```
