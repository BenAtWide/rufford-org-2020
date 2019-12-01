from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "#g$76xn(vz5xn3*_djf#goi@_!(cuovinc0spin25uoqc_=yj#"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES["legacy"] = {
    "ENGINE": "django.db.backends.mysql",
    "NAME": "rufford_org",
    "HOST": "localhost",
    "USER": "root",
    "PASSWORD": "aslkd0923ddll",
}
try:
    from .local import *
except ImportError:
    pass
