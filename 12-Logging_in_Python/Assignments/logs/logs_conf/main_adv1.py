import logging
import logging.config

def setup_logging_from_file():
    # Load config file
    logging.config.fileConfig('logs/logs_conf/logging_adv.conf')
    
    logger = logging.getLogger(__name__)

    # Example logging
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is critical message')

# Testing the function
setup_logging_from_file()