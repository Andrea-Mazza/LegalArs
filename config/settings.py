"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
import sys
import dj_database_url

env_path = Path('.') / '.env'
load_dotenv(dotenv_path='.env')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'userArea.apps.UserareaConfig',
    'tinymce',
    'recuperoCredito.apps.RecuperocreditoConfig',
    'ckeditor',
    # per la sitemap
    'django.contrib.sitemaps',
    'django.contrib.sites',
    # for spaces
    'storages',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DEVELOPMENT_MODE = False

# if DEVELOPMENT_MODE is True:
#     # SECURITY WARNING: keep the secret key used in production secret!
#     SECRET_KEY = env('SECRET_KEY')
#     # SECURITY WARNING: don't run with debug turned on in production!
#     DEBUG = True
#     ALLOWED_HOSTS = ['192.168.1.88',
#                      '127.0.0.1', '192.168.0.167', '192.168.129.248', 'localhost']
#     DJANGO_SETTINGS_MODULE = 'config.settings'
#     EMAIL_BACKEND = env('EMAIL_BACKEND')
#     EMAIL_HOST = env('EMAIL_HOST')
#     EMAIL_HOST_USER = env('EMAIL_HOST_USER')
#     EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
#     EMAIL_PORT = env('EMAIL_PORT')
#     EMAIL_USE_TLS = True
#     EMAIL_USE_SSL = env('EMAIL_USE_SSL')
#     STATIC_URL = 'static/'
#     STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]

#     MEDIA_ROOT = 'static/images'

#     MEDIA_URL = '/images/'
#     STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
#     STRIPE_SECRET_KEY = env('STRIPE_SECRET_KEY')
#     BACKEND_DOMAIN = env('BACKEND_DOMAIN')
#     PAYMENT_SUCCESS_URL = env('PAYMENT_SUCCESS_URL')
#     PAYMENT_CANCEL_URL = env('PAYMENT_CANCEL_URL')
# else:

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False')
ALLOWED_HOSTS = ['legalars-app-9yyw9.ondigitalocean.app', 'localhost']
DJANGO_SETTINGS_MODULE = os.getenv('DJANGO_SETTINGS_MODULE')
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_USE_SSL = False
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = os.getenv('AWS_S3_ENDPOINT_URL')
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_LOCATION)
STATIC_ROOT = 'static'
MEDIA_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, '/blog/')
MEDIA_ROOT = '/images/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
BACKEND_DOMAIN = os.getenv('BACKEND_DOMAIN')
PAYMENT_SUCCESS_URL = os.getenv('PAYMENT_SUCCESS_URL')
PAYMENT_CANCEL_URL = os.getenv('PAYMENT_CANCEL_URL')

if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.getenv("DATABASE_URL")),
    }

EMAIL_SUBJECT_PREFIX = '[Your Project Name]'
PASSWORD_RESET_TIMEOUT_DAYS = 1

AUTH_USER_MODEL = 'userArea.CustomUser'


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'it'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# STATIC_URL = 'static/'
# STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA_ROOT = 'static/images'

# MEDIA_URL = '/images/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# STRIPE_PRICE_ID = os.getenv('STRIPE_PRICE_ID')
# STRIPE_ENDPOINT_SECRET = os.getenv('STRIPE_ENDPOINT_SECRET')
