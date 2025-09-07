import logging

logger = logging.getLogger(__name__) # name will be modules.module_a if package used

def module_a_function():
    logger.info('Module A function started')
    try:
        # placeholder business logic
        value = sum(range(5)) # sample computation
        logger.debug("Module A calculated value=%s",value)
    except Exception as exc:
        logger.exception("Unexpected error in Module A")
    logger.info("Module A function finished")