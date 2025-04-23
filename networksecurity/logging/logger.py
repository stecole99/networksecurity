"""
This Python code sets up a logging system that writes logs to a uniquely named file in a folder called logs.

- logging: Built-in module to track events that happen when software runs.
- os: Module for interacting with the operating system (e.g., creating directories).
- datetime: Used to generate a timestamp for the log file name.

in basicConfig:

- filename: Where to write logs.
- format: 
    How log messages will appear: %(asctime)s = Timestamp
                                  %(lineno)d = Line number in the source code
                                  %(name)s = Logger’s name
                                  %(levelname)s = Log level (INFO, ERROR, etc.)
                                  %(message)s = The actual message

- level=logging.INFO: Records INFO and higher level messages (e.g., WARNING, ERROR)
"""

import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # This creates a filename based on the current date and time

logs_path = os.path.join(os.getcwd(), "logs") # combine current working directory (os.getwd()) with the new directory "logs"
os.makedirs(logs_path,exist_ok = True) # create the directory and if it already exist it does not nothing without raising errors

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)