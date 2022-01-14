#! /usr/bin/env python3

# -----------------------------------------------------------------------------
# mock-logging.py
# -----------------------------------------------------------------------------

# Import from standard library. https://docs.python.org/3/library/

import datetime
import json
import logging
import os
import time

# Code metadata.

__all__ = []
__version__ = "1.0.0"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = '2022-01-14'
__updated__ = '2022-01-14'

log_format = '%(asctime)s %(message)s'

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    # Configure logging. See https://docs.python.org/2/library/logging.html#levels

    log_level_map = {
        "notset": logging.NOTSET,
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "fatal": logging.FATAL,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    # Configuration from environment.

    log_level_parameter = os.getenv("LOG_LEVEL", "info").lower()
    sleep_time = int(os.getenv("SLEEP_TIME", "10"))

    # Logging configuration.

    log_level = log_level_map.get(log_level_parameter, logging.INFO)
    logging.basicConfig(format=log_format, level=log_level)

    # Configuration from environment.

    counter = 0
    while True:
        counter += 1
        message = {
            "counter": counter,
            "timestamp": "{0}".format(datetime.datetime.now()),
            "sleepTime": sleep_time,
        }
        logging.info(json.dumps(message))
        time.sleep(10)
