

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = 'byg83==wb2w!u1ulu1+q=ejh*j76&w0^&c586u45r)@)4hz66r'


DEBUG = True



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'noreply.iiodrones@gmail.com'  
EMAIL_HOST_PASSWORD = 'kckckdiqbymxkhvz'  
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

ALLOWED_HOSTS = ['127.0.0.1', '192.168.29.224', '192.168.29.197']


# Application definition

INSTALLED_APPS = [

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'app',  # register app
    'account',  # register accounts app
    'django.contrib.admin',
    'phonenumber_field',  # app for phone no.
    'django_countries',  # app for countries list
    'payu', # for payment
    'captcha',
    'Blog',
    'ckeditor',
    'store',
    'crispy_forms',
    'jobsportal'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_brotli.middleware.BrotliMiddleware',
    'app.middleware.RoleMiddleware'

]

ROOT_URLCONF = 'myproject.urls'

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
        },
    },
]

AUTH_USER_MODEL = 'account.Account'

WSGI_APPLICATION = 'myproject.wsgi.application'




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'




PAYU_MERCHANT_KEY = "ZaDDqat5" 

PAYU_MERCHANT_SALT = "iCVa7BlTFg"  


PAYU_MODE = "TEST"

PAYU_BASE_URL = "https://sandboxsecure.payu.in/_payment" 




SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CRISPY_TEMPLATE_PACK='bootstrap4'
