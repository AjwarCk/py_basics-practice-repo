import os
import logging
import logging.config
from collections import deque

# import functions from package
from modules.module_a import module_a_function
from modules.module_b import module_b_function
from modules.module_c import module_c_function
from modules.module_d import module_d_function

# Custom console handler that keeps only last N logs
class LastNConsoleHandler(logging.StreamHandler):
    def __init__(self, n=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buffer = deque(maxlen=n)

    def emit(self, record):
        msg = self.format(record)
        self.buffer.append(msg)

        # Clear screen before reprinting (optional)
        print("\033c", end="")
        for line in self.buffer:
            print(line)

def setup_logging(log_file: str="logs/multi_module_app/multi_module_rotating_app.log", level: str="DEBUG"):
    # ensure log folder exist
    os.makedirs(os.path.dirname(log_file),exist_ok=True)

    log_config = {
        "version":1,
        "disable_existing_loggers":False,
        "formatters":{
            "default":{"format":"%(name)s | %(levelname)s | %(asctime)s | %(message)s"},
            "detailed":{"format":"%(name)s <> %(levelname)s <> %(asctime)s <> %(message)s <> %(funcName)s <> %(lineno)d"}
        },
        "handlers":{
            "file":{
                "class":"logging.handlers.RotatingFileHandler",
                "filename":log_file,
                "formatter":"detailed",
                "level":level,
                "maxBytes":1024, # 1KB. max size before rotation
                "backupCount":3 # keep 3 old long files
            },
            "console":{
                "()":"__main__.LastNConsoleHandler", # use custom class 
                "formatter":"default",
                "level":level,
                "n":10 # parameter for buffer size
            }
        },
        "root":{
            "handlers":["file","console"],
            "level":level
        }
    }

    logging.config.dictConfig(log_config)

if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)

    # main function restarts again here
    logger.info('main functions starts')
    logger.debug('main function for loop starts and keeping file under rotating log method')
    # generate some logs to test rotation
    for i in range(100):
        logger.info(f"Log info message: {i}")

    # function module_c
    logger.debug('Main function starts')
    module_c_function()
    module_d_function()
    logger.info('Main function finished')
