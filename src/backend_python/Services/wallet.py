"""This module is used to handle services related to wallets."""

from typing import List
from clases.wallet import Wallet, WalletDao

class WalletService():
    """This class represents the behavior of a service to handle wallet data."""

    def __init__(self):
        """This method initializes the class."""
        self.repository = Wallet()

    def get_wallets(self) -> List[WalletDao]:
        """This method is used to get all the wallets data.
        
        Returns:
           A list with all the wallets data.
        """
        return self.repository.get_wallets() 

    def get_walletid(self, wallet_id: str):
        """This method returns the wallet data."""
        for wallet in self.repository.get_wallets():
            if wallet_id in wallet.wallet_id:
                return wallet

    def current_balance(self, wallet_id: str):
        """This method returns the current balance of a wallet."""
        wallet = self.get_walletid(wallet_id)
        return wallet.balance      

    def add_founds(self, origen_id: str, amount: float, destination_wallet_id: str):
        """This method is used to add funds to a wallet."""
        walleto = self.get_walletid(origen_id)
        walletd = self.get_walletid(destination_wallet_id)
        try:
            if walleto.balance < amount:
                return "Insufficient balance"
            else:
                walleto.balance -= amount
                self.repository.update_wallet(walleto)
                print(f"Wallet origen updated: {walleto}")
                walletd.balance += amount
                self.repository.update_wallet(walletd)
                print(f"Wallet destination updated: {walletd}")
                return "succes"
        except Exception as e:
            print(f"An error occurred with the wallet origen: {e}")
