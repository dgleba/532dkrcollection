"""
Django settings for crmapp project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        err_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured


def node_bin_path(bin_name):
    return os.path.join(BASE_DIR, 'node_modules', '.bin', bin_name)

# ENV_ROLE = get_env_variable('ENV_ROLE')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cc5r6t8u1uu1k-m0(0qghxy-qgkwal@g_x$=(zu=lc2$i$5q1%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pipeline',
    'npm',

    'marketing',
    'subscribers',
    'accounts',
    'contacts',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'crmapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'crmapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'dummy',
#         'USER': 'dummy',
#         'PASSWORD': 'dummy',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': os.getenv('MYSQL_DATABASE'),
             'USER': os.getenv('MYSQL_USER'),
             'HOST': os.getenv('MYSQL_HOST'),
             'PASSWORD':os.getenv('MYSQL_PASSWORD'),
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
    'npm.finders.NpmFinder',
]

PIPELINE = {
    'JAVASCRIPT': {
        'main': {
            'source_filenames': [
                'jquery/dist/jquery.js',
                'bootstrap/dist/js/bootstrap.js',
                'js/app.js',
            ],
            'output_filename': 'bundles/main.js',
        },
    },
    'STYLESHEETS': {
        'main': {
            'source_filenames': [
                'bootstrap/dist/css/bootstrap.css',
                'css/app.css',
            ],
            'output_filename': 'bundles/main.css',
        },
    },
    'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor',
    'YUGLIFY_BINARY': node_bin_path('yuglify'),
    'UGLIFYJS_BINARY': node_bin_path('uglifyjs'),
}

NPM_PREFIX_PATH = BASE_DIR

NPM_FILE_PATTERNS = {
    'bootstrap': ['dist/*'],
    'jquery': ['dist/jquery.js'],
}

STRIPE_SECRET_KEY = 'sk_test_NnRRNgmee1Bzw96ZgYpFfxsM'

STRIPE_PUBLISHABLE_KEY = 'pk_test_3UzQiKTDu8CSlY3GROIb2cpg'

SUBSCRIPTION_PRICE = 1500

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/accounts/list/'
