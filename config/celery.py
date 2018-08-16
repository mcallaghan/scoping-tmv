from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import environ
env = environ.Env()

ROOT_DIR = environ.Path(__file__) - 2
try:
    env_file = str('../../../.env')
    env_file = str(ROOT_DIR.path('.env'))
    print('Loading : {}'.format(env_file))
    env.read_env(env_file)
except:
    print('For production, you will need to generate a .env file. run python env_gen.py')

settings_path = env('DJANGO_SETTINGS_PATH',default='config.settings.local')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_path)


app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(['apps.scoping'])

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
