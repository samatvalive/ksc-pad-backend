
## Django backend for GatherDAO project

This project is built using Django REST Framework to provide the backend API for GatherDAO project.

Below you will find some basic information on how to perform common tasks.<br>

## Table of Contents

-  [Commands](#commands)

-  [FE Migrations](#fe-migrations)

-  [Database configuration](#database-configuration)


## Commands
  		
	This App was created by -	
		django-admin startproject project_name
		
	Install requirements :				
		pip install -r requirements.txt
		
	Migrate :				
		python manage.py makemigrations
		python manage.py migrate
		
	if migate fails to syncDB, try bewlow command
		 python3 manage.py migrate --run-syncdb
		  
	Create superuser/ Admin :				
		 python manage.py createsuperuser
		
	To start django server or to start project :				
		python manage.py runserver
	To start with specific host/port :
		python manage.py runserver 127.0.0.1:8090
	To collect requirements :
			pip3 freeze > requirements.txt 

## FE Migrations

Collect build files from FE project and paste it to backend root project.

## Database Configuration

Provide your database credentials to setting.py as shown in example below :

	
	DATABASES = {
		'default': {
			"ENGINE": "django.db.backends.postgresql_psycopg2",
			"HOST": "ec2-34-254-69-72.eu-west-*************",
			'NAME': 'db_name',
			'USER': 'username',
			'PASSWORD': '******************',
			'PORT': '5432'
			}
		}
