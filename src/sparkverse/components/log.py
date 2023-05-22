"""
info:This module is for logging
autor: Tucudean Adrian-Ionut
date: 22.05.2023
email: Tucudean.Adrian.Ionut@outlook.com
license: MIT
"""
import logging

# Create a logger
logger = logging.getLogger('SIMULATOR')
logger.setLevel(logging.DEBUG)

# Create a console handler
console_handler = logging.StreamHandler()

# Create a custom formatter with color codes
class ColoredFormatter(logging.Formatter):
    """color configuration"""
    def format(self, record):
        # Define color codes for level names
        color_codes = {
            logging.DEBUG: '\033[94m',     # Blue
            logging.INFO: '\033[92m',      # Green
            logging.WARNING: '\033[93m',   # Yellow
            logging.ERROR: '\033[91m',     # Red
            logging.CRITICAL: '\033[91m'   # Red
        }

        # Define color reset code
        color_reset = '\033[0m'

        # Apply color to level name
        levelname = record.levelname
        name=record.name
        colored_levelname = f"{color_codes[record.levelno]}{levelname}{color_reset}"
        colored_name=f"{color_codes[logging.DEBUG]}{name}{color_reset}"
        record.levelname = colored_levelname
        record.name=colored_name

        # Format the log message
        message = super().format(record)

        return message

# Create a colored formatter
formatter = ColoredFormatter('[%(levelname)s] <%(name)s> %(message)s')

# Set the formatter for the console handler
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)

# Log some messages
