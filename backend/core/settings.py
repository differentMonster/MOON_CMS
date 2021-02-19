# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

import os
# from decouple import config
# from unipath import Path
import dj_database_url
import environ
from datetime import timedelta


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_DIR = Path(__file__).parent

# Django enviroment setting
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

# Redirect .env router path
BASE_ENV = environ.Path(__file__) - 2
environ.Env.read_env(env_file=BASE_ENV('.env'))

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_1122')
# SECRET_KEYX=S3cr3t_K#Key
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# load production server from .env
ALLOWED_HOSTS = ['localhost', '127.0.0.1',]

# Application definition
INSTALLED_APPS = [
    'django_pdb',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'app',  # core
    'products', # products
    'accounts', # user account
    'cart', # cart
    'api', # restful api
    'django_countries', # coutries option
    'djoser', # jwt auth
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django_pdb.middleware.PdbMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'core.urls'
LOGIN_REDIRECT_URL = "home"   # Route defined in app/urls.py
LOGOUT_REDIRECT_URL = "home"  # Route defined in app/urls.py
TEMPLATE_DIR = os.path.join(BASE_DIR, "core/templates")  # ROOT dir for templates

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

# Development Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Devolopment Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Production Database - [POSTGRES]
# DATABASES = {
#     "default": {
#         "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
#         "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
#         "USER": os.environ.get("SQL_USER", "user"),
#         "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
#         "HOST": os.environ.get("SQL_HOST", "localhost"),
#         "PORT": os.environ.get("SQL_PORT", "5432"),
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

LOGIN_URL = "/api/v1/signin"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
    # 'AUTH_HEADER_TYPES' :( 'JWT' ),
    'ROTATE_REFRESH_TOKENS': True, # IMPORTANT
    'BLACKLIST_AFTER_ROTATION': True # IMPORTANT
}

# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://127.0.0.1'
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#############################################################
# SRC: https://devcenter.heroku.com/articles/django-assets

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

# Media files (Products Images)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'core/static'),
)
#############################################################
#############################################################


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework_simplejwt.authentication.JWTAuthentication"],
    # "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    # "TEST_REQUEST_DEFAULT_FORMAT": "json",
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.DjangoModelPermissions",),
}

# add
AUTH_USER_MODEL = 'accounts.user'
