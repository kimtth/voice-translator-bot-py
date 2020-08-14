import logging


def set_logging(logname):
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    filename = './' + logname + '.log'
    handler = logging.FileHandler(filename, mode='a', encoding='utf-8')
    handler.setFormatter(formatter)

    logger = logging.getLogger(logname)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger