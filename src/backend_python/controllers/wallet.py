"""This module is used to define some endpoints to handle wallets data."""

from typing import List
from fastapi import APIRouter, HTTPException
from Services.wallet import WalletService
from repositories.wallet import WalletDao
from repositories.creditcard import CreditCard
from Services.user import create_wallet

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


@router.get("/wallet/{wallet_id}/balance")
def show_current_balance(wallet_id: str):
    """This endpoint is used to get the current balance of a wallet."""
    balance = services.show_current_balance(wallet_id)
    return {"balance": balance}


@router.get("/wallet/{wallet_id}/transactions")
def show_transactions(wallet_id: str):
    """This endpoint is used to show the transactions of a wallet."""
    services.show_transactions(wallet_id)


@router.post("/wallet/{wallet_id}/add_credit_card/")
def add_credit_card(wallet_id: str, credit_card: CreditCard):
    """This endpoint is used to add a credit card to a wallet."""
    try:
        services.add_credit_card(wallet_id, credit_card)
        return {"message": "Credit card added successfully"}
    except Exception:
        raise HTTPException(
            status_code=400, detail="An error occurred while adding the credit card"
        )


@router.get("/wallet/{wallet_id}/show_credit_card/")
def show_credit_card(wallet_id: str):
    """This endpoint is used to show the credit card of a wallet."""
    credit_card = services.show_credit_card(wallet_id)
    return credit_card


@router.post("/wallet/{wallet_origen_id}/send_founds/{wallet_destination_id}/{amount}")
def send_founds(wallet_origen_id: str, amount: float, wallet_destination_id: str):
    """This endpoint is used to add funds to a wallet."""
    operation = services.send_founds(wallet_origen_id, amount, wallet_destination_id)
    if operation == "Insufficient balance":
        raise HTTPException(status_code=400, detail="Insufficient balance")
    elif operation == "succes":
        return {"message": "Funds added successfully"}
    else:
        raise HTTPException(
            status_code=400, detail="An error occurred while adding the funds"
        )


@router.post("/wallet/{wallet_id}/create_pocket/Savings")
def create_saving_pocket(
    wallet_id: str, pocket_id: str, pocket_name: str, amount: float, pocket_type_ = "savings"
):
    """This endpoint is used to create a pocket."""
    try:
        services.create_pocket(pocket_id, wallet_id, pocket_type_, pocket_name, amount)
        return {"message": "Pocket created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as ex:
        raise HTTPException(
            status_code=400, detail="An error occurred while creating the pocket"
        )

@router.post("/wallet/{wallet_id}/create_pocket/Investments")
def create_invest_pocket(
    wallet_id: str, pocket_id: str, pocket_name: str, amount: float, pocket_type_ ="investments"
):
    """This endpoint is used to create a pocket."""
    try:
        services.create_pocket(pocket_id, wallet_id, pocket_type_, pocket_name, amount)
        return {"message": "Pocket created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as ex:
        raise HTTPException(
            status_code=400, detail="An error occurred while creating the pocket"
        )

@router.post("/wallet/{wallet_id}/create_pocket/Bills")
def create_bills_pocket(
    wallet_id: str, pocket_id: str, pocket_name: str, amount: float, pocket_type_ = "bills"
):
    """This endpoint is used to create a pocket."""
    try:
        services.create_pocket(pocket_id, wallet_id, pocket_type_, pocket_name, amount)
        return {"message": "Pocket created successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as ex:
        raise HTTPException(
            status_code=400, detail="An error occurred while creating the pocket"
        )


@router.get("/wallet/{wallet_id}/pockets/")
def show_pockets(wallet_id: str):
    """This endpoint is used to show the pockets of a wallet."""
    pockets = services.show_pockets(wallet_id)
    return pockets

@router.post("/wallet/{wallet_id}/add_founds_pocket/{pocket_id}/")
def add_founds_pocket(wallet_id: str, pocket_id: str, amount: float):
    """This endpoint is used to add funds to a pocket."""
    try:
        services.add_founds_pocket(wallet_id, pocket_id, amount)
        return {"message": "Funds added successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as ex:
        raise HTTPException(
            status_code=400, detail="An error occurred while adding the funds"
        )

@router.post("/Register")
def register_wallet(answer: bool, user_id: str):
    """This endpoint is used to create a wallet."""
    try:
        create_wallet(answer, user_id)
        return {"message": "Wallet created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail="An error occurred while creating the wallet")

@router.post("/wallet/{wallet_id}/add_founds/{amount}")
def add_founds(wallet_id: str, amount: float):
    """This endpoint is used to add funds to a pocket."""
    try:
        services.add_founds(wallet_id, amount)
        return {"message": "Funds requested successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as ex:
        raise HTTPException(
            status_code=400, detail="An error occurred while requesting the funds"
        )