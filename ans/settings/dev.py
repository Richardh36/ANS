from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$_%gpp^6j!0u49h%u*c1yor65uv35v$509#)5hfz*bn=(ib9uv'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
