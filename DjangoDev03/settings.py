"""
Django settings for DjangoDev03 project.

Generated by 'django-admin startproject' using Django 3.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0qgx5+#ej(s!y&#xz%0^7&g_onma($v%gentp_0ksgzaxo6jp7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # 引入DRF框架
    'projects.apps.ProjectsConfig', # 子应用添加应用名.apps.应用名Config
    'interfaces.apps.InterfacesConfig',
    'django_filters' # 过滤引擎添加
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware', # 自己注释是因为post请求时总是提示：CSRF验证失败. 请求被中断
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DjangoDev03.urls'

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

WSGI_APPLICATION = 'DjangoDev03.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 指定数据库引擎
        'ENGINE':'django.db.backends.mysql',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME':'dev03', # 指定数据库名
        'USER':'root', # 数据库用户名
        'PASSWORD':'root', # 数据库密码
        'HOST':'localhost', # 数据库主机域名或者ip
        'PORT':'3306' # 数据库端口号
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    # 默认响应渲染类
    'DEFAULT_RENDERER_CLASSES': [
        # Json渲染器为第一优先级
        'rest_framework.renderers.JSONRenderer',
        # 可浏览的API渲染器为第二优先级--不需要可以注释掉即可
        # 'rest_framework.renderers.TemplateHTMLRenderer',
    ],
    # 默认过滤引擎，默认路径
    "DEFAULT_FILTER_BACKENDS":
        [
            'django_filters.rest_framework.backends.DjangoFilterBackend', # 过滤引擎路径
            'rest_framework.filters.OrderingFilter' # 排序引擎路径
        ],
    # 全局指定分页引擎类
    'DEFAULT_PAGINATION_CLASS':
        # 'rest_framework.pagination.PageNumberPagination',
        'utils.pagination.ManualPageNumberPagination',
    # 一定要指定每页获取的条数
    'PAGE_SIZE': 3,
}

