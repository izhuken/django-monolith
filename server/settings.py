from os import getenv as env
from os import path
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Environ settings
# https://django-environ.readthedocs.io/en/latest/

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-vakb02ds@g(izf(x-3pf@_+_98ypnequy*9h3_7!37@tx+9w6(' #os.getenv('SECRET_KEY')
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(env("DEBUG")))

ALLOWED_HOSTS = [
    '0.0.0.0', 
    '127.0.0.1',
    'localhost',
    'kitten.labofdev.ru',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # second part
    'whitenoise',
    'drf_yasg',
    'corsheaders',
    'rest_framework',

    # third part
    'app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # whitenoise
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # cors headers
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME'),
            'USER': env('DB_USER'),
            'PASSWORD': env('DB_PASSWORD'),
            'HOST': env('DB_HOST'),
            'PORT': int( env('DB_PORT') ),
        }
    }

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    path.join(STATIC_ROOT, 'app'),
]

# Media
# https://docs.djangoproject.com/en/4.1/topics/files/

MEDIA_ROOT = path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# All-Auth configutation
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SITE_ID = 1


# Cors Headers Settings
# https://github.com/adamchainz/django-cors-headers

CORS_ALLOW_ALL_ORIGINS = True 

# WhiteNoise settings
# https://github.com/evansd/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

### DAJNGO SECURITY
# https://docs.djangoproject.com/en/4.1/topics/security/

# XFrame options
# https://docs.djangoproject.com/en/4.1/ref/clickjacking/

# X_FRAME_OPTIONS = 'SAMEORIGIN'

# CSRF settings
# https://docs.djangoproject.com/en/4.1/ref/csrf/
 
CSRF_COOKIE_SECURE = False

# XSS settings
# https://docs.djangoproject.com/en/4.1/topics/security/#cross-site-scripting-xss-protection

SECURE_BROWSER_XSS_FILTER = False

# SSL& HSTS settings
# https://docs.djangoproject.com/en/4.1/topics/security/#ssl-https

SECURE_SSL_REDIRECT = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Session settings
# https://docs.djangoproject.com/en/4.1/topics/http/sessions/#settings

SESSION_COOKIE_SECURE = False

# Secure content settings

SECURE_CONTENT_TYPE_NOSNIFF = False