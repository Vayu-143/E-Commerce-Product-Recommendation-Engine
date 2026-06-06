import logging

logging.basicConfig(
    filename="outputs/app.log",
    level=logging.INFO,
    format=(
        "%(asctime)s - "
        "%(levelname)s - "
        "%(message)s"
    )
)


def log_event(message):

    logging.info(message)