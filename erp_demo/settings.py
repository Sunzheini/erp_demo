import os.path
from os.path import join
from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.urls import reverse_lazy
# from decouple import config, Csv


"""
Using Heroku CLI for the env vars:

write the vars inside Settings -> Reveal Config Vars
write them in settings.py with os.environ.get('VAR_NAME') 
install file from heroku site
heroku login, it will open the browser
`D:\Study\Projects\PycharmProjects\erp_demo>heroku config -a erp-demo` to see the config vars
`D:\Study\Projects\PycharmProjects\erp_demo>heroku logs --tail -a erp-demo` to see the logs in the console
"""

"""
Switch this to True if you use local vars and to False if you use heroku vars
"""
LOCAL_VARS = False


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# if LOCAL_VARS:
#     SECRET_KEY = config('SECRET_KEY')
# else:
#     SECRET_KEY = os.environ.get('SECRET_KEY')


SECRET_KEY = os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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
    'erp_demo.interaction_mng',
    'erp_demo.resource_mng',
    'erp_demo.operations_mng',
    'erp_demo.nonconformity_mng',
    'erp_demo.actions_mng',
    'erp_demo.newactions_mng',
    'erp_demo.actionplan_mng',
    'erp_demo.maintenance_mng',
    'erp_demo.calibration_mng',
    'erp_demo.control_plan_mng',
    'erp_demo.characteristics_mng',
    'erp_demo.defect_cat_mng',
    'erp_demo.statistics_mng',
    'erp_demo.review_mng',
    'erp_demo.analytics',

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


# if LOCAL_VARS:
#     # local
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql',
#             'NAME': 'erp_demo_db',  # same name as the DB created
#             'USER': 'postgres-user',
#             'PASSWORD': 'password',
#             'HOST': 'localhost',  # Not host.docker.internal - only for pgadmin
#             'PORT': '5432',
#         }
#     }
# else:
#     # heroku
#     DATABASES = {
#         'default': {
#             'ENGINE': os.environ.get('DB_ENGINE'),
#             'NAME': os.environ.get('DB_NAME'),
#             'USER': os.environ.get('DB_USER'),
#             'PASSWORD': os.environ.get('DB_PASSWORD'),
#             'HOST': os.environ.get('DB_HOST'),
#             'PORT': os.environ.get('DB_PORT'),
#         }
#     }

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}


# without heroku
# CACHES = {
#     'default': {
#         'BACKEND':
#             'django.core.cache.backends.redis.RedisCache',
#         'LOCATION':
#             'redis://127.0.0.1:6379',
#     }
# }


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

# info for translation
"""
put {% load i18n %} in the template
replace text with {% trans "text" %} in the template

python manage.py makemessages -l bg     # get the messages with {%trans  %} in the .po file
translate the messages in the .po file, remove the #fuzzy
python manage.py compilemessages        # apply translations

translate forms, upload button language, choices 
    (like customers/models.py and customers/forms.py)
"""

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media_files'

# needed for cloudinary
# if LOCAL_VARS:
#     CLOUDINARY_STORAGE = {
#         'CLOUD_NAME': config('CLOUD_NAME'),
#         'API_KEY': config('API_KEY'),
#         'API_SECRET': config('API_SECRET'),
#     }
# else:
#     CLOUDINARY_STORAGE = {
#         'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
#         'API_KEY': os.environ.get('API_KEY'),
#         'API_SECRET': os.environ.get('API_SECRET'),
#     }

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUD_NAME'),
    'API_KEY': os.environ.get('API_KEY'),
    'API_SECRET': os.environ.get('API_SECRET'),
}

# also correction in models and the links for the file in templates


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')

# this is needed for the custom user model
AUTH_USER_MODEL = 'user_mng.AppUser'

"""
Create superuser:
python manage.py createsuperuser
"""
