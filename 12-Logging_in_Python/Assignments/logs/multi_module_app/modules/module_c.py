
import logging

logger = logging.getLogger(__name__) # name will be modules.module_c if package used

def module_c_function():
    logger.info('Module C function started')
    try:
        # placeholder business logic
        value = sum(range(5)) # sample computation
        logger.debug('Module C function calculated value=%s',value)
    except Exception as exc:
        logger.exception('Unexpected error occured Module C')
    logger.info('Module C function finished')