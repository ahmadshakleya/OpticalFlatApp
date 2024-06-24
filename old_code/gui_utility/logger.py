import logging

def setup_logger():
    logger = logging.getLogger('OpticalFlatApp')
    logger.setLevel(logging.DEBUG)  # Set to DEBUG to capture all levels of log messages

    # Create a file handler which logs even debug messages
    fh = logging.FileHandler('optical_flat_app.log')
    fh.setLevel(logging.DEBUG)

    # Create a console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
