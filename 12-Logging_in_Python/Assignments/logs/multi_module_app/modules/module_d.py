import logging

logger = logging.getLogger(__name__) # name will be modules.module_d if package used

def module_d_function():
    logger.info('Module D function started')

    try:
        # placeholder business logic
        text = 'hello'.upper()
        logger.debug('Module D processed text=%s',text)
    except Exception as e:
        logger.exception('Unexpected error occured in Module D')
    logger.info('Module D function finished')