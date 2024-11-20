"""
Django settings for food_story project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nb4_vvst#(_z!@jqqvx9mk2*ye046_7=j2n*8dyj@ojgt@sjnh'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    
    'Core',
    'Story',
    'Account',
    
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

ROOT_URLCONF = 'food_story.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'Account.context_processors.footer_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'food_story.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

if DEBUG:
    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'Account.CustomUser'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]




JAZZMIN_SETTINGS = {
    "site_title": "Mənim Admin Panelim",  # Brauzer sekmesinde görsənəcək ad
    "site_header": "Mənim Adminim",  # Admin başlığı
    "site_brand": "Brand Adı",  # Admin panelinin yuxarısında göstəriləcək brend
    "welcome_sign": "Xoş gəlmisiniz!",  # Admin girişində göstərilən mesaj
    "copyright": "© 2024 Mənim Şirkətim",  # Panelin aşağı hissəsində copyright məlumatı
    "topmenu_links": [  # Üst menyuya linklər əlavə etmək üçün
        {"name": "Ana Səhifə", "url": "/", "permissions": ["auth.view_user"]},
        {"app": "auth"},  # "auth" tətbiqinə keçid
    ],
    "usermenu_links": [  # İstifadəçi menyusuna keçidlər əlavə etmək üçün
        {"name": "Profilim", "url": "/profile", "new_window": True},
    ],
    "show_sidebar": True,  # Yan menyunun göstərilib-göstərilməməsi
    "navigation_expanded": True,  # Menyuların avtomatik genişlənməsi
    "hide_apps": ["sessions"],  # Göstərilməyəcək tətbiqlər
    "hide_models": ["auth.Group"],  # Göstərilməyəcək modellər
}

JAZZMIN_SETTINGS["changeform_format"] = "horizontal_tabs"
JAZZMIN_SETTINGS["changeform_format_overrides"] = {"auth.user": "collapsible"}
JAZZMIN_UI_TWEAKS = {
    "theme": "cerulean",  # Mövcud bootstrap temaları: cerulean, cosmo, flatly, və s.
    "dark_mode_theme": "cosmo",  # Tünd tema üçün
    "navbar_small_text": True,
    "body_small_text": True,
    "accent": "accent-primary",
    "button_classes": {"primary": "btn-outline-primary", "secondary": "btn-outline-secondary"},
}
JAZZMIN_SETTINGS["custom_css"] = "css/custom.css"


# Yalnız inkişaf mühiti üçün e-poçtları konsola yazdırın
# settings.py - E-poçt Göndərmə Ayarları

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Gmail SMTP serveri
EMAIL_PORT = 587  # TLS üçün port
EMAIL_USE_TLS = True  # TLS şifrələməsindən istifadə et
EMAIL_HOST_USER = 'your_email@gmail.com'  # Gmail istifadəçi adı
EMAIL_HOST_PASSWORD = 'your_email_password'  # Gmail şifrəniz (2FA istifadə edirsinizsə, tətbiq şifrəsi istifadə edin)
DEFAULT_FROM_EMAIL = 'your_email@gmail.com'  # Göndərən e-poçt ünvanı
