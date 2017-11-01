import logging
import os

from celery import Celery
from celery.signals import setup_logging


app = Celery('app')
app.conf.update({
    'broker_url': os.environ['CELERY_BROKER_URL'],
    'imports': ('tasks',),
    'task_serializer': 'json',
    'result_serializer': 'json',
    'accept_content': ['json'],
    'worker_hijack_root_logger': False,
    'result_compression': 'gzip',
    'timezone': 'UTC'})


@setup_logging.connect
def setup_loggers(*args, **kwargs):
    logger = logging.getLogger()
    formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] [%(processName)s] %(message)s [%(lineno)d]')

    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
