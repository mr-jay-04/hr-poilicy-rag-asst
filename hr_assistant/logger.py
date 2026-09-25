"""
Shared logger used by every other step

Every module in this app asks this file for a logger instead of setting up its own. That way all logs
(from document loading to the final answer) end up in one place, in one consistent format.
"""

import logging
import os
from datetime import datetime

current_date = datetime.now().strftime("%d %B").lower()

parent_dir = "logs"
path = os.path.join(parent_dir, current_date)
os.makedirs(path, exist_ok=True)
_run_started_at = datetime.now().strftime("%Y%m%d-%H%M%S")
RUN_LOG_FILE = os.path.join(path, f"run_{_run_started_at}.log")

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers = [
        logging.FileHandler(RUN_LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ],
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)