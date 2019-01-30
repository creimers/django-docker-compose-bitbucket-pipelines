import os
import sys
import celery

from django.conf import settings


if "runserver" in sys.argv:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.env.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.env.production")


app = celery.Celery("celery_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
