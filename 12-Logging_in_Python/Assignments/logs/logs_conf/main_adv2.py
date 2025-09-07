import logging
import logging.config
from collections import deque
import sys

class RingBufferConsoleHandler(logging.Handler):
    def __init__(self, capacity=10):
        super().__init__()
        self.buffer = deque(maxlen=capacity)

    def emit(self, record):
        msg = self.format(record)
        self.buffer.append(msg)
        self._print_buffer()

    def _print_buffer(self):
        print("\n--- Last 10 logs ---")
        for log in list(self.buffer):
            print(log)

# Load the config file
logging.config.fileConfig('logs/logs_conf/logging_adv.conf')

logger = logging.getLogger()

# Remove default consoleHandler to prevent duplicate output
for handler in logger.handlers[:]:
    if isinstance(handler, logging.StreamHandler):
        logger.removeHandler(handler)

# Add custom console handler
console_handler = RingBufferConsoleHandler(capacity=10)
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# Example: Generate multiple logs to see last 10 printed
for i in range(15):
    logger.debug(f'Debug message {i}')
    logger.info(f'Info message {i}')
    logger.warning(f'Warning message {i}')
    logger.error(f'Error message {i}')
    logger.critical(f'Critical message {i}')
