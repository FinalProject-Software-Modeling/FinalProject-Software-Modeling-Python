"""This is the Main module of the application."""

import uvicorn
from fastapi import FastAPI

from controllers.wallet import router as wallet_router

app = FastAPI(
    title="Wallets API",
    description="This is an API to handle wallets data.",
    version="0.1"
)

app.include_router(wallet_router)

if __name__ == "__main__": 
    uvicorn.run(app, host="localhost", port=8000)