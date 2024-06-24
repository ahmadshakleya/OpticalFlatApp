import logging

def setup_logger():
    logger = logging.getLogger('OpticalFlatApp')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('optical_flat_app.log')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
