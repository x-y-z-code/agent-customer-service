
from datetime import datetime
import logging
import logging.handlers
import os

from utils.path_tool import get_abs_path


LOG_ROOT =  get_abs_path("logs")
os.makedirs(LOG_ROOT,exist_ok=True)

DEFAULT_LOG_FROMAT =  logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s"
)

def get_log(
  name:str="agent",
  console_levl:int=logging.INFO,
  file_levl:int = logging.DEBUG,
  log_file = None      
)->logging.Logger:
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    # if logging.handlers:
    #     return log
    

    console_handlers =  logging.StreamHandler()
    console_handlers.setLevel(console_levl)
    console_handlers.setFormatter(DEFAULT_LOG_FROMAT)

    log.addHandler(console_handlers)

    if not log_file:
        log_file = os.path.join(LOG_ROOT,F"{name}_{datetime.now().strftime('%Y%m%d')}.log")
    file_handler = logging.FileHandler(log_file,encoding="utf-8")
    file_handler.setLevel(file_levl)
    file_handler.setFormatter(DEFAULT_LOG_FROMAT)
    log.addHandler(file_handler)
    return log

logger = get_log()


