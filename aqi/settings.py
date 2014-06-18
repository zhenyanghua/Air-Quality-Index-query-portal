"""
Django settings for aqi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Set paths
fillPath = lambda x: os.path.join(os.path.dirname(__file__), x)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    fillPath('templates'),
)

TEMPLATE_CONTEXT_PROCESSORS=(
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

EXCEL_SUPPORT = 'xlwt' # or 'openpyxl' or 'pyexcelerator'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hk3o@7ntpnf(7c7n1xgo&4x=r@62249y+w+szz-7rtv^2hs%!!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.gis',
    'search',
    'django_tables2',
    'django_tables2_reports',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'aqi.urls'

WSGI_APPLICATION = 'aqi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE':'django.contrib.gis.db.backends.postgis',
        'NAME': 'XXX',
        'USER': 'XXX',
        'PASSWORD': 'XXX',
        'HOST': 'XXX',
        'PORT': 'XXX',
        #'OPTIONS': {'client_encoding': 'UTF8', },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
##    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
##    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

