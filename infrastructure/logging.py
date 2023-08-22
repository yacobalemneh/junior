import logging

class Logging:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def log(self, message):
        logging.info(message)