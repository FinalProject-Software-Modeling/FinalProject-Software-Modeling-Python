"""This file is a module that contains the Wallet class."""

import json
from typing import List, Dict, Optional
from pydantic import BaseModel
from repositories.creditcard import CreditCard
from environment_variables import EnvironmentVariables


class WalletDao(BaseModel):
    """This class is used to define deta structure related to wallets."""

    wallet_id: str
    balance: float
    movements: dict
    credit_card: Optional[CreditCard] = None
    status: str
    pockets: Optional[List[Dict]] = None

class Wallet:
    """This class represents the behavior os a repository to handle  wallet data."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """This method is used to create a singleton instance of the class."""
        if cls._instance is None:
            cls._instance = super(Wallet, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """This method initializes the class."""
        if not hasattr(self, "_initialized"):
            env = EnvironmentVariables()
            path_file = env.wallets_data
            self.load_data(path_file)
            self._initialized = True

    def load_data(self, path_file: str):
        """This method is used to load the data from the database."""
        try:
            with open(path_file, "r", encoding="utf-8") as file:
                self.data = json.load(file)
                print(f"Data loaded successfully: {path_file}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            self.data = []

    def get_wallets(self) -> List[WalletDao]:
        """This method is used to get all the wallets data.

        Returns:
           A list with all the wallets data.
        """
        wallets = []
        for wallet in self.data:
            wallet_temp = WalletDao(
                wallet_id=wallet["wallet_id"],
                balance=wallet["balance"],
                movements=wallet["movements"],
                credit_card=wallet["credit_card"],
                status=wallet["status"],
                pockets=wallet["pockets"],
            )
            wallets.append(wallet_temp)
        return wallets

    def update_wallet(self, wallet: WalletDao):
        """This method is used to update the wallet data."""
        for i, wallet_temp in enumerate(self.data):
            if wallet.wallet_id in wallet_temp["wallet_id"]:
                self.data[i] = wallet.dict()
                break
        self.save_data()

    def save_data(self):
        """This method is used to save the data into the database."""
        env = EnvironmentVariables()
        path_file = env.wallets_data
        try:
            with open(path_file, "w", encoding="utf-8") as file:
                json.dump(self.data, file, indent=4)
                print(f"Data saved successfully: {path_file}")
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
