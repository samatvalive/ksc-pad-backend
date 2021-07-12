from decouple import config

DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": config('DATABASE_HOST'),
        "NAME": config('DATABASE_NAME'),
        "USER": config('DATABASE_USER'),
        "PASSWORD": config('DATABASE_PASSWORD'),
        "PORT": config('DATABASE_PORT')
    }
}

SECURE_SSL_REDIRECT = False
DEBUG = True

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

ALLOWED_HOSTS = [
    'gatherdao.com'
]
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = [
    'http://gatherdao.com',
    'http://www.gatherdao.com',
]

# RATELIMIT SETTINGS
RATELIMIT_ENABLE = config('RATELIMIT_ENABLE', cast=bool)
