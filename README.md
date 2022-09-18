


Update the environment(create .env file in root directory)
.env Example:

    SECRET_KEY = 'django-secret'
    POSTGRES_DB=inforcetest
    DB_PORT=5432
    DB_USER=postgres
    DB_PASSWORD=12345
    
    
Getting Started without docker



change settings.py (databases host must be '127.0.0.1')
Install requirements.
Create migrations and apply them into database.
Run server

Getting Started with docker



run in terminal:
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose up
open website 127.0.0.1:8000



