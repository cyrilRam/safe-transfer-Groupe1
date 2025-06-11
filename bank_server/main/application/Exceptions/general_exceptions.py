import logging
from typing import Type

from fastapi import HTTPException

from bank_server.main.webapi.middlewares.logger import logger


class CustomException(HTTPException):
    def __init__(self, status_code: int, detail: str, log_level: int):
        super().__init__(status_code=status_code, detail=detail)
        self.log_level = log_level
        logger.log(self.log_level, f"Custom error {type(self).__name__} occurred: {self.detail}")


class ObjectNotFoundException(CustomException):
    def __init__(self, object_type: Type, id_object: str):
        detail = f"The {object_type.__name__} with id {id_object} doesn't exist"
        super().__init__(status_code=404, detail=detail, log_level=logging.ERROR)


class SafeTransferException(CustomException):
    def __init__(self, dto_type: Type, reason: str):
        detail = f"Échec du virement sécurisé pour {dto_type.__name__} : {reason}"
        super().__init__(status_code=502, detail=detail, log_level=logging.ERROR)


class ErrorConnectionDBException(CustomException):
    def __init__(self, message):
        detail = f"The connection to the db has failed. {message} "
        super().__init__(status_code=503, detail=detail, log_level=logging.ERROR)
