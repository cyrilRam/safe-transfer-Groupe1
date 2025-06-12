import time

from fastapi import Request
from fastapi.responses import JSONResponse

from bank_server.main.application.Exceptions.general_exceptions import CustomException
from bank_server.main.webapi.middlewares.logger import logger


async def exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


async def custom_middleware(request: Request, call_next):
    start_time = time.time()
    try:
        response = await call_next(request)

        process_time = time.time() - start_time
        # Check if response status indicates an error (4xx or 5xx)
        if 400 <= response.status_code < 600:
            logger.error(
                f"Request {request.method} {request.url.path} completed in {process_time:.2f} seconds with status {response.status_code}")
        else:
            logger.info(
                f"Request {request.method} {request.url.path} completed in {process_time:.2f} seconds with status {response.status_code}")
        return response
    except Exception as e:
        process_time = time.time() - start_time
        logger.error(f"process_time : {process_time} - Unhandled exception: {e}")
        return JSONResponse(
            status_code=500,
            content={"detail": str(e)},
        )