from django.conf import  settings
from backend.settings.components import  config, BASE_DIR

DEBUG = False

ALLOWED_HOSTS = [
    config('DOMAIN_NAME'),
    config('IP'),

    # We need this value for `healthcheck` to work:
    'localhost',
]

AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS
AWS_STORAGE_BUCKET_NAME = settings.AWS_STORAGE_BUCKET
AWS_S3_REGION_NAME = settings.AWS_S3_REGION
AWS_DEFAULT_ACL = None
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'



# DATABASES = {
#
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('POSTGRES_DB'),
#         'USER': config('POSTGRES_USER'),
#         'PASSWORD': config('POSTGRES_PASSWORD'),
#         'HOST': config('POSTGRES_HOST'),
#         'PORT': '5432',
#
#     }
#
# }