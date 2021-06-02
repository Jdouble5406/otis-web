"""
Django settings for otisweb project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).parent.parent.absolute()
ENV_PATH = PROJECT_ROOT / '.env'
if ENV_PATH.exists():
	load_dotenv(ENV_PATH)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

## Manually added settings

CRISPY_TEMPLATE_PACK = 'bootstrap4'
HIJACK_ALLOW_GET_REQUESTS = True
HIJACK_LOGIN_REDIRECT_URL = '/'
HIJACK_LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'

PRODUCTION = bool(os.getenv('IS_PRODUCTION'))
if not PRODUCTION:
	INTERNAL_IPS = ('127.0.0.1',)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = not bool(os.getenv('IS_PRODUCTION'))

# SECURITY WARNING: App Engine's security features ensure that it is safe to
# have ALLOWED_HOSTS = ['*'] when the app is deployed. If you deploy a Django
# app not on App Engine, make sure to set an appropriate host here.
# See https://docs.djangoproject.com/en/1.10/ref/settings/
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
	'core',
	'dashboard',
	'exams',
	'roster',
	'arch',
	'otisweb',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.humanize',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'bootstrap4',
	'crispy_forms',
	'hijack_admin',
	'hijack',
	'compat',
	'import_export',
	'reversion',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'otisweb.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
			],
		'debug' : not PRODUCTION,
		},
	},


]

WSGI_APPLICATION = 'otisweb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if os.getenv("DATABASE_NAME"):
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.mysql',
			'NAME' : os.getenv("DATABASE_NAME"),
			'USER' : os.getenv("DATABASE_USER"),
			'PASSWORD' : os.getenv("DATABASE_PASSWORD"),
			'HOST' : os.getenv("DATABASE_HOST"),
			'PORT' : '5432',
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

if PRODUCTION:
	DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
	STATIC_URL = os.getenv("STATIC_URL")
	GS_BUCKET_NAME = os.getenv("GS_BUCKET_NAME")
	MEDIA_URL = os.getenv("MEDIA_URL")
	import import_export.tmp_storages
	IMPORT_EXPORT_TMP_STORAGE_CLASS = import_export.tmp_storages.CacheStorage
	SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
else:
	STATIC_URL = '/static/'
	MEDIA_URL = '/media/'
	SECRET_KEY = 'evan_chen_is_really_cool'
INVOICE_HASH_KEY = os.getenv("INVOICE_HASH_KEY", "evan_chen_is_still_really_cool")

FILE_UPLOAD_HANDLERS = ('django.core.files.uploadhandler.MemoryFileUploadHandler',)
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760 # 10MB
