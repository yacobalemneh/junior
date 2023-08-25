from core.config import Config

import coloredlogs

def setup_logging():
    config = Config()
    coloredlogs.install(level=config.LOGGING_LEVEL, fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
def setup():
    setup_logging()