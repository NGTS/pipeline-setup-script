import logging

logging.basicConfig(level=logging.WARNING, format='%(message)s')


def get_logger(name):
    return logging.getLogger(name)
