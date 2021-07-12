from decouple import config
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        # "ENGINE": "django.db.backends.postgresql_psycopg2",
        # "HOST": "ec2-54-74-77-126.eu-west-1.compute.amazonaws.com",
        # 'NAME': 'ddotlu8archegp',
        # 'USER': 'mruztjasakiils',
        # 'PASSWORD': 'ebc9cae2ad4b555a990d537ffc9041296068ce7e68a78a996754766e0e8e974b',
        # 'PORT': '5432'

        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True
SECURE_SSL_REDIRECT = False
ALLOWED_HOSTS = ['127.0.0.1',
                 'gatherdao.herokuapp.com',
                 'www.gatherdao.herokuapp.com'
                 ]
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:3001',
    'http://127.0.0.1:3000',
]
