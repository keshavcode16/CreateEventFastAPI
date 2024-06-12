import random
import uuid
from datetime import datetime, timedelta
from typing import Union

from fastapi import Response, status
from app.config import settings
from app.logs.log_handler import LibLogger

log: LibLogger = LibLogger()

def exception_decorator(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            response: Response = Response()
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            log.error(error)
            return False, error

    return inner

def generate_uuid() -> str:
    return str(uuid.uuid4())

