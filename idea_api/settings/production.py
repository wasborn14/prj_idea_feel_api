from .base import *

DEBUG = False

ALLOWED_HOSTS = ['160.251.42.169', 'ideafeels.net']

# アクセス許可
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "https://idea-feel.com/",
]

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'database1',
    'USER': 'wasborn',
    'PASSWORD': 'password',
    'HOST': 'localhost',
    'PORT': '',
    }
}

