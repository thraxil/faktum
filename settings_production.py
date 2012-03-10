from settings_shared import *

TEMPLATE_DIRS = (
    "/var/www/faktum/faktum/templates",
)

MEDIA_ROOT = '/var/www/faktum/uploads/'
# put any static media here to override app served static media
STATICMEDIA_MOUNTS = (
    ('/sitemedia', '/var/www/faktum/faktum/sitemedia'),	
)

COMPRESS_ROOT = "/var/www/faktum/faktum/media/"
DEBUG = False
TEMPLATE_DEBUG = DEBUG

try:
    from local_settings import *
except ImportError:
    pass
