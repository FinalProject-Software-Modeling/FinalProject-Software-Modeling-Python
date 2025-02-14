"""This module is used to define some auxiliar_services for the application."""
from repositories.wallet import WalletDao, Wallet

def create_wallet(answer: bool, user_id: str):
    """This function is used to create a wallet."""
    if answer is True:
        wallet_id_ = user_id + "-01"
        new_wallet = WalletDao(
            wallet_id= wallet_id_,
            balance= 0.0,
            movements={},
            credit_card=None,
            status="active",
            pockets=None
        )

        wallet = Wallet()
        wallet.data.append(new_wallet.dict())
        wallet.save_data()
        print(f"Wallet {wallet_id_} created successfully")
