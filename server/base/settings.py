"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname(PROJECT_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0x(o)#=@*nhtq+qo=fb@(gylwo7v_n-tq(z#g-62#u%sreq9v9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # viewflow
    # 'viewflow.frontend',
    # 'viewflow',

    # material
    'material',
    'material.frontend',
    # 'material.admin',

    # wechat app
    # 'wechat_django',

    'jet',

    # standard django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # wagtail setting
    # 'wagtail.contrib.forms',
    # 'wagtail.contrib.redirects',
    # 'wagtail.embeds',
    # 'wagtail.sites',
    # 'wagtail.users',
    # 'wagtail.snippets',
    # 'wagtail.documents',
    # 'wagtail.images',
    # 'wagtail.search',
    # 'wagtail.admin',
    # 'wagtail.core',
    # 'wagtail.api.v2',
    'taggit',
    'modelcluster',

    'rest_framework',
    'django_filters',
    'drf_yasg',

    # celery integration
    'djcelery_email',
    'django_celery_beat',

    # wagtail setting
    # 'cms',

    # my apps
    'lib',
    'api.apps.ApiConfig',
    'control.apps.ControlConfig',
    'demo.apps.DemoConfig',
    'dashboard.apps.DashboardConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # wagtail setting
    # 'wagtail.core.middleware.SiteMiddleware',
    # 'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'material.frontend.context_processors.modules',
            ],
            # 必须添加，否则报错
            'builtins': [
                'material.templatetags.material_form',
            ],
            'debug': True,
            # 自定义tags
            'libraries': {
                'base_debug': 'base.templatetags.base_debug',
                'data_filter': 'base.templatetags.data_filter',
                'display_lang_name': 'base.templatetags.display_lang_name',
            },
        },
    },
]

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
# LANGUAGE_CODE = 'zh-hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'


USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en-us', 'English'),
    ('zh-hans', '中文'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
    # os.path.join(PROJECT_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


SITE_ID = 1

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    )
}

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
#
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"
WAGTAIL_SITE_NAME = 'My Site Base'
LOGIN_REDIRECT_URL = '/app/dashboard'
LOGOUT_REDIRECT_URL = '/login'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s] %(levelname)s %(filename)s[%(module)s:%(funcName)s:%(lineno)d] %(message)s',
            # 'datefmt': "%Y/%m/%d %H:%M:%S",
        },
        'celery': {
            'format': '[%(asctime)s] %(levelname)s %(filename)s[%(module)s:%(funcName)s:%(lineno)d] %(message)s',
            # 'datefmt': "%Y/%m/%d %H:%M:%S",
        },
    },
    'handlers': {
        'console': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': sys.stdout
        },
        'tasks': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
            'formatter': 'celery',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'default': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
        'tasks': {
            'handlers': ['tasks'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
    'root': {
        'handlers': ['console',],
        'level': 'INFO',
        'propagate': True
    }
}


# for celery
CELERY_BROKER_URL = os.environ.get('APP_CELERY_BROKER_URL', default='redis://localhost:6379/9')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_IGNORE_RESULT = True
CELERY_ENABLE_UTC = True
# 长时间运行Celery有可能发生内存泄露，可以像下面这样设置
CELERY_MAX_TASKS_PER_CHILD = 40 # 每个worker执行了多少任务就会死掉
# 任务执行最长时间60分钟 #IR2NB
CELERY_TASK_SOFT_TIME_LIMIT = 3600
CELERY_TASK_TIME_LIMIT = 3600
CELERY_TIMEZONE = 'Asia/Shanghai'
# 重复任务解决
# CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 28800}

# 制定特定任务路由到特定执行队列
# CELERY_TASK_ROUTES = {
#     'picker.tasks.checker': {'queue': 'trans'},
#     'picker.tasks.retry_monitor': {'queue': 'retries'},
#     'witness.tasks.counter': {'queue': 'witness'},
#     'api.tasks.*': {'queue': 'api'},
#     'picker.tasks.retry_worker': {'queue': 'retries'},
#     'witness.tasks.erc20_withdraw': {'queue': 'erc20_withdraw'},
#     'witness.tasks.get_erc20_withdraw_pending_trans': {'queue': 'erc20_withdraw'},
# }
#
# CELERY_TASK_QUEUES = {
#     "trans": {
#         "exchange": "trans"
#     },
#     'witness': {
#         'exchange': 'witness'
#     },
#     'api': {
#         'exchange': 'api'
#     },
#     'retries': {
#         'exchange': 'retries'
#     },
#     'cron': {
#         'exchange': 'cron'
#     },
#     'erc20_withdraw': {
#         'exchange': 'erc20_withdraw'
#     }
# }

