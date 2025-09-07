import logging
import logging.config

# Load config file
logging.config.fileConfig('logs/logs_conf/logging_adv.conf')

logger = logging.getLogger() # root logger

# Example logging
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is critical message')