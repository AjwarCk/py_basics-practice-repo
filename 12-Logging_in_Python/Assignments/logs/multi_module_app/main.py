import os
import logging
import logging.config

# import functions from package modules
from modules.module_a import module_a_function
from modules.module_b import module_b_function

def setup_logging(log_file: str='logs/multi_module_app/modules/multi_module_app.log', level: str='DEBUG'):
    # ensure log folder exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    log_config = {
        "version": 1,
        "disable_existing_loggers": False, # Keep third-party
        "formatters": {
            "default": {
                "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            },
            "detailed": {
                "format": "%(asctime)s | %(name)s | %(levelname)s | %(funcName)s | %(lineno)d | %(message)s"
            }
        },
        "handlers":{
            "file":{
                "class":"logging.FileHandler",
                "filename":log_file,
                "formatter":"detailed",
                "level":level
            },
            "console":{
                "class":"logging.StreamHandler",
                "formatter":"default",
                "level":level
            }
        },
        "root":{
            "handlers":['file','console'],
            "level":level
        }
    }

    logging.config.dictConfig(log_config)

if __name__ == "__main__":
    setup_logging() # configure logging once, at startup
    logger = logging.getLogger(__name__) # __name__ is '__main__' when run directly

    logger.info('Main module started')
    module_a_function()
    module_b_function()
    logger.info('Main module finished')