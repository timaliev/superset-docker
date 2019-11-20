import os

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': 'redis',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': 1,
    'CACHE_REDIS_URL': 'redis://redis:6379/1'}
SQLALCHEMY_DATABASE_URI = 'sqlite:////var/lib/superset/db/superset.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'thisISaSECRET_1234'

BASE_DIR = os.getenv('SUPERSET_HOME', '/var/lib/superset')

# The file upload folder, when using models with files
UPLOAD_FOLDER = BASE_DIR + '/uploads/'

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = BASE_DIR + '/uploads/'
