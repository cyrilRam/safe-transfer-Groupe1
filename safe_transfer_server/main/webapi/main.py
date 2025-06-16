from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from safe_transfer_server.main.webapi.config.get_config import ConfigurationSafeTransfer
from safe_transfer_server.main.webapi.controllers import user_controllers, interbank_transaction_controllers,chat_ia_controller
from safe_transfer_server.main.webapi.middlewares.logger import logger
from safe_transfer_server.main.webapi.middlewares.middleware import custom_middleware

load_dotenv()
var = ConfigurationSafeTransfer.get_config_var()
allowed_urls = var["AllowedUrls"]

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=custom_middleware)

app.include_router(user_controllers.router)
app.include_router(interbank_transaction_controllers.router)
app.include_router(chat_ia_controller.router)

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

    uvicorn.run("__main__:app", host="localhost", port=8081, reload=True)
