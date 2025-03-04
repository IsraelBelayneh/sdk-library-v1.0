import os
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logger():
    logger = logging.getLogger("SDKLogger")
    logger.setLevel(logging.DEBUG)

    # Create logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Create a timed rotating file handler
    file_handler = TimedRotatingFileHandler(
        f"logs/sdk.log",
        when="midnight",  # Rotate at midnight
        interval=1,       # Every day
        backupCount=7     # Keep 7 days of logs
    )
    
    # Set formatter for the file handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Add a stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger

# Create a logger instance
logger = setup_logger()
