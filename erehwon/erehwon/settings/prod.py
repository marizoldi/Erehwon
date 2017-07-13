from erehwon.settings import *
import dj_database_url

DEBUG = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECRET_KEY = os.environ["dummyDEVkeyReplaceMeinPROD!"]
ALLOWED_HOSTS = ['erehwon.herokuapp.com']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = os.environ["SENDGRID_USERNAME"]
EMAIL_HOST_PASSWORD = os.environ["SENDGRID_PASSWORD"]
EMAIL_PORT = 587
EMAIL_USE_TLS = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
        'erehwon': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
