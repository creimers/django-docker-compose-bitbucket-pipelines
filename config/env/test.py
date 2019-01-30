from .. import *

DEBUG = False

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CELERY_TASK_ALWAYS_EAGER = True
