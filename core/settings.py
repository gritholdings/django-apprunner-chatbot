"""
Django settings for chatbot project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import json
import os
from pathlib import Path

# e.g. "example.com"
DOMAIN_NAME = "meetgrit.com"

# Basics

## Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

## Load the credentials.json file
with open(os.path.join(BASE_DIR, 'credentials.json')) as f:
    credentials = json.load(f)

## Set a default value of 'DEV' if the environment variable is not found
DJANGO_ENV = os.getenv('DJANGO_ENV', 'DEV')

## Assign the secret key from the JSON file
SECRET_KEY = credentials['SECRET_KEY']

## Debug mode
if DJANGO_ENV == 'PROD':
    DEBUG = False
else:
    DEBUG = True
DEBUG = True

ALLOWED_HOSTS = [".awsapprunner.com", "." + DOMAIN_NAME, "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'chatbot_app',
    'home',
    'customauth'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database is AWS RDS Aurora PostgreSQL

with open(os.getcwd() + '/credentials.json') as f:
    credentials = json.load(f)
    DATABASE_PASSWORD = credentials['DATABASE_PASSWORD']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME':'postgres',
            'USER':'postgres',
            'PASSWORD': DATABASE_PASSWORD,
            'HOST':'database-1-instance-1.cpwpdhxjx3in.us-east-1.rds.amazonaws.com',
            'PORT':'5432'
        }
    }

# Authentication

## User Authentication
AUTH_USER_MODEL = 'customauth.CustomUser'

AUTHENTICATION_BACKENDS = [
    'customauth.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend'
]

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


## Password validation
## https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators
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

## REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}

## CORS
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:3000',
    "https://*.awsapprunner.com",
    "https://platform." + DOMAIN_NAME
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",
    "https://*.awsapprunner.com",
    "https://*." + DOMAIN_NAME
]

### Add CORS_EXPOSE_HEADERS to ensure CSRF token is exposed
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']

### Configure CSRF settings
CSRF_COOKIE_SECURE = True  # For HTTPS
CSRF_COOKIE_SAMESITE = 'Lax'  # Or 'None' if you need cross-site requests
CSRF_COOKIE_DOMAIN = "." + DOMAIN_NAME  # Include subdomain
CSRF_USE_SESSIONS = False  # Store CSRF token in cookie instead of session
CSRF_COOKIE_HTTPONLY = False  # Allow JavaScript access to CSRF token

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'