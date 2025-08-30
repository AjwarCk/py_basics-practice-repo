import logging
import os

def setup_logger(name,logfile,level,fmt):
    '''
    Create and configures a logger with a FileHandler + shared ConsoleHandler.
    Args:
        name(str): Logger name
        logfile(str): File to write logs
        level(int): Minimum logging level
        fmt(str): Log format string
    '''

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handler
    if not logger.handlers:
        # File Handler
        fh = logging.FileHandler(logfile)
        fh.setLevel(level)
        fh.setFormatter(logging.Formatter(fmt))
        logger.addHandler(fh)

        # Console Handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(logging.Formatter('>>> %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(ch)

    return logger

# Root logger config (run always)
logging.basicConfig(filename='logs/ecom4/app_root.log',
                    level=logging.DEBUG,
                    format='%(asctime)s | %(name)s | %(levelname)s | %(message)s'
                    )

# These loggers are created at import time
auth_logger = setup_logger('auth','logs/ecom4/auth.log',logging.INFO,
                           '%(asctime)s - AUTH - %(levelname)s - %(message)s')

orders_logger = setup_logger('orders','logs/ecom4/orders.log',logging.WARNING,
                             '%(asctime)s - ORDERS - %(levelname)s - %(message)s')

inventory_logger = setup_logger('inventory','logs/ecom4/inventory.log',logging.DEBUG,
                                '%(asctime)s - INVENTORY - %(levelname)s - %(message)s')

# Example workflow (only when run directly)
if __name__ == "__main__":
    #1. User log in
    auth_logger.info("User 'Amy' has log in")
    auth_logger.warning("Supicious login attempt from IP 192.168.1.50")

    #2. User places order
    orders_logger.info("Order #1234 placed by 'Amy'")
    orders_logger.error("Payment failed for order #1234: card declined")

    #3. Inventory check
    inventory_logger.debug("Stock checked for product #5678")
    inventory_logger.warning("Low stock alert for product #5678: Only 2 left")

    #4. Root catches everything
    logging.error("Unexpected exception: Database connection lost")