import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY', 'SET THIS!')

if os.environ.get('ADMIN_NAME'):
    ADMINS = ((os.environ['ADMIN_NAME'], os.environ['ADMIN_EMAIL']),)
    MANAGERS = ADMINS

if os.environ.get('SERVER_EMAIL'):
    SERVER_EMAIL = os.environ['SERVER_EMAIL']

if os.environ.get('EMAIL_HOST'):
    EMAIL_HOST = os.environ['EMAIL_HOST']
    EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))

if os.environ.get('UPWORK_PUBLIC_KEY'):
    UPWORK_KEYS = {
        'public_key': os.environ['UPWORK_PUBLIC_KEY'],
        'secret_key': os.environ['UPWORK_SECRET_KEY'],
        'oauth_access_token': os.environ['UPWORK_OAUTH_ACCESS_TOKEN'],
        'oauth_access_token_secret': os.environ['UPWORK_OAUTH_ACCESS_TOKEN_SECRET']
    }
    UPWORK_PROFILE_ID = os.environ['UPWORK_PROFILE_ID']  # client.provider_v2.search_providers(data={'q': 'Dionyz Lazar'})
else:
    print('Set UPWORK_PUBLIC_KEY, UPWORK_SECRET_KEY, UPWORK_OAUTH_ACCESS_TOKEN, UPWORK_OAUTH_ACCESS_TOKEN_SECRET,  UPWORK_PROFILE_ID env variables for this to work!')

UPWORK_DATA_TIMEOUT = 60*60*24

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'django_cache',
        'TIMEOUT': None,
    }
}

DEBUG = False

ALLOWED_HOSTS = ['.dionysio.com']

APPEND_SLASH = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.admin',

    'compressor',
    'honeypot',

    'base',
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

ROOT_URLCONF = 'portfolio.urls'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

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
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/Bratislava'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/


HONEYPOT_FIELD_NAME = 'last_name'

STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

LOGGING = {}

import django_heroku
django_heroku.settings(locals(), staticfiles=False)

LOGGING['loggers'][''] = {
    'handlers': ['console'],
    'level': 'INFO'
}
LOGGING['loggers']['django'] = {
    'handlers': ['console'],
    'level': 'INFO'
}

STATIC_ROOT = '/app/static/'
STATIC_URL = '/static/'

MEDIA_ROOT = '/app/media/'
MEDIA_URL = '/media/'
