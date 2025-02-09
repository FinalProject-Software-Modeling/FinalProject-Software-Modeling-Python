"""This module is used to define some endpoints to handle wallets data."""

from typing import List
from fastapi import APIRouter, HTTPException
from Services.wallet import WalletService
from clases.wallet import WalletDao

router = APIRouter()

services = WalletService()

@router.get("/wallets_Db")
def get_wallets() -> List[WalletDao]:
    """This endpoint is used to get all the wallets data."""
    return services.get_wallets()

@router.get("/wallet/{wallet_id}")
def get_wallet(wallet_id: str):
    """This endpoint is used to get the wallet data."""
    wallet = services.get_walletid(wallet_id)
    if wallet:
        return wallet
    raise HTTPException(status_code=404, detail="Wallet not found")

@router.put("/wallet/{wallet_origen_id}/add_founds/{wallet_destination_id}/")
def add_founds(wallet_origen_id: str, amount: float, wallet_destination_id: str):
    """This endpoint is used to add funds to a wallet."""
    operation = services.add_founds(wallet_origen_id, amount, wallet_destination_id)
    if operation == "Insufficient balance":
        raise HTTPException(status_code=400, detail="Insufficient balance")
    elif operation == "succes":
        return {"message": "Funds added successfully"}
    else:
        raise HTTPException(status_code=400, detail="An error occurred while adding the funds")
