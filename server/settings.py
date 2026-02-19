from os import getenv, path
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(getenv("DEBUG")))

APP_MODE = getenv("APP_MODE")

ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
] + getenv("DOMAIN", "localhost").split(",")


# Application definition

INSTALLED_APPS = [
    # 1st party apps
    "ckeditor",
    # 2d party apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3d party apps
    "automobile.apps.AutomobileConfig",
    "info.apps.InfoConfig",
    "products.apps.ProductsConfig",
    "vacancies.apps.VacanciesConfig",
    # API
    "api.apps.ApiConfig",
]

MIDDLEWARE = [
    # "settings.middlewares.UnicodeDomainMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "settings.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "settings.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

if APP_MODE == "production":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": getenv("POSTGRES_DB"),
            "USER": getenv("POSTGRES_USER"),
            "PASSWORD": getenv("POSTGRES_PASSWORD"),
            "HOST": getenv("POSTGRES_HOST"),
            "PORT": int(getenv("POSTGRES_PORT")),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

if DEBUG:
    STATICFILES_DIRS = [path.join(BASE_DIR, "static")]
else:
    STATIC_ROOT = path.join(BASE_DIR, "static")
    STATICFILES_DIRS = []


# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media
# https://docs.djangoproject.com/en/5.2/topics/files/

MEDIA_ROOT = path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

### DAJNGO SECURITY
# https://docs.djangoproject.com/en/5.2/topics/security/

# XFrame options
# https://docs.djangoproject.com/en/5.2/ref/clickjacking/

X_FRAME_OPTIONS = "SAMEORIGIN"

# XSS settings
# https://docs.djangoproject.com/en/5.2/topics/security/#cross-site-scripting-xss-protection

SECURE_BROWSER_XSS_FILTER = True

# SSL& HSTS settings
# https://docs.djangoproject.com/en/5.2/topics/security/#ssl-https

SECURE_SSL_REDIRECT = APP_MODE == "production"
SECURE_HSTS_INCLUDE_SUBDOMAINS = APP_MODE == "production"
SECURE_HSTS_PRELOAD = APP_MODE == "production"

# Session settings
# https://docs.djangoproject.com/en/5.2/topics/http/sessions/#settings

SESSION_COOKIE_SECURE = APP_MODE == "production"

# Secure content settings

SECURE_CONTENT_TYPE_NOSNIFF = APP_MODE == "production"

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}

# Cache settings

if DEBUG:
    CACHE_LIFETIME = 60
else:
    CACHE_LIFETIME = 3600
