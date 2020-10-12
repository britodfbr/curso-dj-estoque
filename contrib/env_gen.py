# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
"""
Django SECRET_KEY generator.
"""
from string import ascii_lowercase, digits
from pathlib import Path
from django.utils.crypto import get_random_string

chars = ascii_lowercase + digits + '!@#$%^&*(-_=+)'

CONFIG_STRING = f"""
DEBUG=True
SECRET_KEY={get_random_string(50, chars)}
ALLOWED_HOSTS=127.0.0.1, .localhost
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=
#EMAIL_PORT=
#EMAIL_USE_TLS=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
"""

# Writing our configuration file to '.env'
configfile = Path('.env')
configfile.write_text(CONFIG_STRING)
