from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from bank_server.main.webapi.config.get_config import Configuration
from bank_server.main.webapi.controllers import user_controller, account_controller, transaction_controller
from bank_server.main.webapi.middlewares.logger import logger
from bank_server.main.webapi.middlewares.middleware import custom_middleware

load_dotenv()
var = Configuration.get_config_var()
allowed_urls = var["AllowedUrls"]

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=custom_middleware)

app.include_router(user_controller.router)
app.include_router(account_controller.router)
app.include_router(transaction_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_urls,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info('bank_server is running')
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("__main__:app", host="localhost", port=8080, reload=True)
