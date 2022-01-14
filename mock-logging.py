#! /usr/bin/env python3

# -----------------------------------------------------------------------------
# mock-logging.py
# -----------------------------------------------------------------------------

# Import from standard library. https://docs.python.org/3/library/

import datetime
import json
import logging
import os
import random
import time

# Code metadata.

__all__ = []
__version__ = "1.0.0"  # See https://www.python.org/dev/peps/pep-0396/
__date__ = '2022-01-14'
__updated__ = '2022-01-14'

log_format = '%(asctime)s %(message)s'

# Message templates with variables.

log_templates = [
    "{level}: Starting {sdp}",
    "{level}: Not sure if {sdp} is correct",
    "{level}: {sdp} starting to slow down",
    "{level}: Monitoring {sdp}",
    "{level}: Unexpected use of {sdp}",
    "{level}: Results for {sdp}:  x: {xval} y: {yval}",
    "{level}: {sdp} nearing threshold of {xval}",
]

# List of Software Design Patterns from  https://en.wikipedia.org/wiki/Software_design_pattern

software_design_patterns = [
    "Abstract factory",
    "Active Object",
    "Adapter",
    "Adapter",
    "Balking",
    "Binding properties",
    "Blackboard",
    "Bridge",
    "Builder",
    "CPU atomic operation",
    "Chain of responsibility",
    "Command",
    "Composite"
    "Compute kernel",
    "Decorator"
    "Dependency Injection",
    "Double-checked locking",
    "Event-based asynchronous",
    "Extension object"
    "Facade",
    "Factory method",
    "Flyweight",
    "Front controller",
    "Guarded suspension",
    "Interpreter",
    "Iterator",
    "Join",
    "Lazy initialization",
    "Lock",
    "Marker",
    "Mediator",
    "Memento",
    "Message design pattern",
    "Module",
    "Monitor object",
    "Multiton",
    "Null object",
    "Object pool",
    "Observer",
    "Prototype",
    "Proxy",
    "Reactor",
    "Read-write lock",
    "Resource acquisition is initialization",
    "Save Conncurrency with Exclusive Ownership",
    "Scheduler",
    "Servant",
    "Singleton",
    "Specification",
    "State",
    "Strategy",
    "Template method",
    "Thread pool",
    "Thread-specific storage",
    "Twin",
    "Visitor",
]

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
    application_id = os.getenv("APPLICATION_ID", "default")

    # Logging configuration.

    log_level = log_level_map.get(log_level_parameter, logging.INFO)
    logging.basicConfig(format=log_format, level=log_level)

    # Configuration from environment.

    counter = 0
    while True:
        counter += 1

        # Determine value for "level".

        level = "Info"
        random_percent = random.randint(0, 100)
        if random_percent < 1:
            level = "Fatal"
        elif random_percent < 3:
            level = "Error"
        elif random_percent < 7:
            level = "Warning"

        # Craft "message_id"

        message_id = "mock-{:08}".format(random.randint(0, 100))

        # Format message.

        sdp = random.choice(software_design_patterns)
        xval = random.randint(0, 9999)
        yval = random.randint(0, 9999)

        log_template = random.choice(log_templates)
        message = log_template.format(**globals())

        # Assemble log message.

        log_message = {
            "applicationId": application_id,
            "counter": counter,
            "level": level,
            "message": message,
            "messageId": message_id,
            "sleepTime": sleep_time,
            "timestamp": "{0}".format(datetime.datetime.now()),
        }

        logging.info(json.dumps(log_message))
        time.sleep(sleep_time)
