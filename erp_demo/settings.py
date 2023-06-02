import os.path
from os.path import join
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7h3u-2kr%214m7&ar3r6zd9567tgpccxloqkaj!v_apc)q6rnz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'erp-demo.herokuapp.com',
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'erp_demo.main_app',
    'erp_demo.dox_mng',
    'erp_demo.process_mng',
    'erp_demo.hr_mng',
    'erp_demo.organization_mng',
    'erp_demo.customer_mng',
    'erp_demo.user_mng',
    'erp_demo.supplier_mng',
    'erp_demo.tools',
    'erp_demo.api',
    'erp_demo.kpi_mng',
    'erp_demo.risk_mng',
    'erp_demo.opportunity_mng',

    'cloudinary',
]

MIDDLEWARE = [
    # comment when not needed
    'erp_demo.custom_logic.middleware.measure_time_middleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.locale.LocaleMiddleware', # for translation
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'erp_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'erp_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# heroku
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd65ftbcmnuhf23',
#         'USER': 'vjawodyzjlcaes',
#         'PASSWORD': '82857bf4d38383e6dc3686a412a753ffb103a4452cedd21be4da436e46a962fa',
#         'HOST': 'ec2-52-19-55-12.eu-west-1.compute.amazonaws.com',
#         'PORT': '5432',
#     }
# }

# without heroku
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'erp_demo_db',         # same name as the DB created
        'USER': 'postgres-user',
        'PASSWORD': 'password',
        'HOST': 'localhost',    # Not host.docker.internal - only for pgadmin
        'PORT': '5432',
    }
}

# heroku
# not connected

# without heroku
# CACHES = {
#     'default': {
#         'BACKEND':
#             'django.core.cache.backends.redis.RedisCache',
#         'LOCATION':
#             'redis://127.0.0.1:6379',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'bg'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Europe/Sofia'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'translations'),
]

LANGUAGES = [
    ('en', 'English'),
    ('bg', 'Bulgarian'),
]

"""
put {% load i18n %} in the template
replace text with {% trans "text" %} in the template
python manage.py makemessages -l bg     # get the messages with {%trans  %} in the .po file
translate the messages in the .po file, remove the #fuzzy
python manage.py compilemessages        # apply translations

translate forms, upload button language, choices 
    (like customers/models.py and customers/forms.py)
"""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media_files'

# needed for cloudinary
cloudinary.config(
    cloud_name="hpnglbxlz",
    api_key="713429118316855",
    api_secret="veB_dwVAE954b9yeyx3rCUNnV2o",
    secure=True,
)
# also correction in models and the links for the file in templates


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')

# this is needed for the custom user model
AUTH_USER_MODEL = 'user_mng.AppUser'
