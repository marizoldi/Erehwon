from erehwon.settings import *
import dj_database_url

DEBUG = True

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = ['erehwon-dev.herokuapp.com']
