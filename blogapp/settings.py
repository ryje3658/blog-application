import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'w10u@0!1k(w@h&=re6yc2t!ullm0hrqizibwmzrr2lyyk(_+my'

DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = [
    'ckeditor',
    'ckeditor_uploader',
    'profiles',
    'blog',
    'crispy_forms',
    'authentication',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
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

ROOT_URLCONF = 'blogapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                os.path.join(BASE_DIR, 'authentication','templates'),
                os.path.join(BASE_DIR, 'blog', 'templates'),
                os.path.join(BASE_DIR, 'profiles', 'templates'),
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

#TEMPLATE_CONTEXT_PROCESSORS += ("custom_app.context_processors.categories_processor", )
TEMPLATES[0]['OPTIONS']['context_processors'].append("blog.context_processors.categories_processor")

WSGI_APPLICATION = 'blogapp.wsgi.application'


"""Database"""
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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = "/"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

CRISPY_TEMPLATE_PACK = 'bootstrap4'

"""ID needed for Django-allauth social integration"""

SITE_ID = 1


"""Static and media files"""

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static_cdn'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_cdn/')

"""Email settings."""

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '#'
EMAIL_HOST_PASSWORD = '#'

"""CKeditor settings. (Text editor.)"""

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = 'pillow'
