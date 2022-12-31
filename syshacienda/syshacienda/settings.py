"""
Django settings for syshacienda project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import mimetypes
from django.conf import ENVIRONMENT_VARIABLE

# Build paths inside the project like this: BASE_DIR / 'subdir'.
mimetypes.add_type("text/javascript", ".js", True)
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v$g592%*cac^5qnbc_d=ca3jfkwe)f(wrtboqb46*xk0=6du=9'

# SECURITY WARNING: don't run with debug turned on in production!


ENVIRONMENT_VARIABLE = 'dev' #'production'

ALLOWED_HOSTS = ['127.0.0.1','*']

DEBUG = True
if ENVIRONMENT_VARIABLE != 'production':
    DEBUG = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'baseapp',
    'mnt',
    'vent',
    'api',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'syshacienda.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates'), ],
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

WSGI_APPLICATION = 'syshacienda.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if ENVIRONMENT_VARIABLE != 'production':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'syshacienda',
            #'OPTIONS': {
            #    'options' : " -c search_path=public"
            #},
            'USER': 'postgres',
            'PASSWORD': 'sa',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        },
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'syshacienda',
            #'OPTIONS': {
            #    'options' : " -c search_path=public"
            #},
            'USER': 'super',
            'PASSWORD': 'sa-uae-Syshaciend1',
            'HOST': 'cesarorrala-2907.postgres.pythonanywhere-services.com',
            'PORT': '12907',#'5432',
        },
    }
    


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

MEDIA_ROOT = (os.path.join(BASE_DIR,'media'),)
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIR = os.path.join(BASE_DIR,'static')
STATIC_ROOT = os.path.join(BASE_DIR,'static')

#STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

#MEDIA_ROOT = os.path.join(BASE_DIR, "media")
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

