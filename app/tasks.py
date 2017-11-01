from celery.utils.log import get_task_logger
from worker import app


logger = get_task_logger(__name__)


@app.task(bind=True, name='do_something')
def do_something(self):
    pass
