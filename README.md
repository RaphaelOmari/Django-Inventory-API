**Technologies:**
- **Django 3.2+**
- **psycopg2 2.9.9**
- **PostgreSQL 17**
- **Bootstrap 5** for UI styling
- **Python 3.11**



**Set Up Virtual Environment**
python:

 > python -m venv venv
 > source venv/bin/activate



**Create PostgreSQL Database**
bash:

psql -U postgres
CREATE DATABASE inv_store_db;
CREATE USER my_db_user WITH PASSWORD 'my_db_password';
ALTER ROLE my_db_user SET client_encoding TO 'utf8';
ALTER ROLE my_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE my_db_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE inv_store_db TO my_db_user;

**Update settings.py to connect to Database**
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inv_store_db',
        'USER': 'my_db_user',
        'PASSWORD': 'set_password',
        'HOST': 'localhost',
        'PORT': '5432', #Ensure this default port is used
    }
}


**Apply Migrations**
bash:

python manage.py makemigrations
python manage.py migrate


**--------------TO RUN PROJECT-----------------------------**

bash:

python manage.py createsuperuser

python manage.py migrate

python manage.py runserver
