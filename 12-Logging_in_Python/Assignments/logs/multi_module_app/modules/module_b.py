import logging

logger = logging.getLogger(__name__)

def module_b_function():
    logger.info('Module B function started')
    try:
        # placeholder business logic
        text = "hello".upper()
        logger.debug('Module B processed text=%s', text)
    except Exception as e:
        logger.exception('Unexception in Module B')
    logger.info("Module B function finished")