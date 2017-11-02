import logging
from flask import Flask

stream = logging.StreamHandler()
stream.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s [%(lineno)d]'))
logging.getLogger().addHandler(stream)
logging.getLogger().setLevel(logging.DEBUG)


app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/")
def index():
    return '', 204


if __name__ == "__main__":
    logger.info('Starting app')
    app.run()