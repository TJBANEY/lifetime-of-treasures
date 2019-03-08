from lifetimeoftreasures.settings.base import *

STATIC_ROOT = os.path.join(BASE_DIR, 'lifetimeoftreasures/static/')

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}

# DEFAULT_FILE_STORAGE = 'filebrowser_s3.storage.S3MediaStorage'
#
# AWS_ACCESS_KEY_ID = 'AKIAIJBXVIFBPRROKEBA'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'lifetimeoftreasures'
#
# AWS_LOCATION = 'us-east-2'
# FILEBROWSER_DIRECTORY = AWS_LOCATION
#
# MEDIA_ROOT = ''
#
# AWS_S3_CUSTOM_DOMAIN = 'lifetimeoftreasures'
# if AWS_S3_CUSTOM_DOMAIN is None:
#     MEDIA_URL = '...your public AWS bucket URL with protocol and trailing slash'
# else:
#     MEDIA_URL = 'https://s3.console.aws.amazon.com/s3/buckets/lifetimeoftreasures/'