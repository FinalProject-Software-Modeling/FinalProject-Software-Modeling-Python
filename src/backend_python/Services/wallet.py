"""This module is used to handle services related to wallets."""

from typing import List
from datetime import datetime
from repositories.wallet import Wallet, WalletDao
from repositories.creditcard import CreditCard
from repositories.transaction import Transaction
from repositories.factory_pockets import PocketFactory


class WalletService:
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

    def show_current_balance(self, wallet_id: str):
        """This method returns the current balance of a wallet."""
        wallet = self.get_walletid(wallet_id)
        return wallet.balance

    def add_transaction(self, wallet_id: str, transaction: Transaction):
        """This method is used to add a transaction to a wallet."""
        wallet = self.get_walletid(wallet_id)
        movements = wallet.movements
        print("Succesfull movements loaded")

        if movements:
            print("CHECKING LAST TRANSACTION")
            last_transaction = max(
                movements.values(),
                key=lambda t: datetime.strptime(t["date"], "%Y-%m-%d %H:%M:%S"),
            )
            last_id_reference = last_transaction["id_reference"]
            print(f"ultima transaccion: {last_transaction}")
            print(f"Last transaction id: {last_id_reference}")
            last_id_p = last_id_reference.split("-")
            select_last_element = last_id_p[-1]
            number = int(select_last_element) + 1
            new_complement = str(number)
            transaction.id_reference = wallet_id + "-" + new_complement
            wallet.movements[transaction.id_reference] = transaction
            self.repository.update_wallet(wallet)

        else:
            print("SAVING TRANSACTION")
            last_id_reference = transaction.id_reference + "-0"
            print(f"Last transaction id: {last_id_reference}")
            transaction.id_reference = last_id_reference
            wallet.movements[transaction.id_reference] = transaction
            self.repository.update_wallet(wallet)

    def show_transactions(self, wallet_id: str):
        """This method is used to show all the transactions of a wallet."""
        wallet = self.get_walletid(wallet_id)
        return wallet.movements

    def add_credit_card(self, wallet_id: str, credit_card: CreditCard):
        """This method is used to add a credit card to a wallet."""
        wallet = self.get_walletid(wallet_id)
        wallet.credit_card = credit_card
        self.repository.update_wallet(wallet)
        print(f"Credit card added to wallet: {wallet}")

    def show_credit_card(self, wallet_id: str):
        """This method is used to show the credit card of a wallet."""
        wallet = self.get_walletid(wallet_id)
        return wallet.credit_card

    def send_founds(self, origen_id: str, amount: float, destination_wallet_id: str):
        """This method is used to add funds to a wallet."""
        walleto = self.get_walletid(origen_id)
        walletd = self.get_walletid(destination_wallet_id)
        try:
            if walleto.balance < amount:
                return "Insufficient balance"
            else:
                walleto.balance -= amount
                self.repository.update_wallet(walleto)
                actual_date = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print(f"Actual date: {actual_date}")
                self.add_transaction(
                    walleto.wallet_id,
                    Transaction(
                        id_reference=walleto.wallet_id + "FS",
                        wallet_id=walleto.wallet_id,
                        type_="send founds",
                        amount=amount,
                        date=actual_date,
                        where_to=walletd.wallet_id,
                        description=f"Sended ${amount} to {walletd.wallet_id}",
                    ),
                )
                print("Wallet origen updated")
                walletd.balance += amount
                self.repository.update_wallet(walletd)
                print("Wallet destination updated")
                actual_date = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                print(f"Actual date: {actual_date}")
                self.add_transaction(
                    walletd.wallet_id,
                    Transaction(
                        id_reference=walleto.wallet_id + "FR",
                        wallet_id=walleto.wallet_id,
                        type_="receive founds",
                        amount=amount,
                        date=actual_date,
                        where_to=walletd.wallet_id,
                        description="Received ${amount} from {walleto.wallet_id}",
                    ),
                )
                return "succes"
        except Exception as e:
            print(f"An error occurred with the wallet origen: {e}")

    def request_founds(
        self, request_wallet_id: str, amount: float, destination_wallet_id: str
    ):
        """This method is used to request funds from a wallet."""

    def create_pocket(
        self,
        pocket_id: str,
        wallet_id: str,
        pocket_type: str,
        pocket_name: str,
        amount: float,
    ):
        """This method is used to create a pocket."""
        wallet = self.get_walletid(wallet_id)
        if not wallet.pockets:
            wallet.pockets = []

        if amount > wallet.balance:
            print("Insufficient balance, the pocket will be created with 0 amount")
            amount = 0

        new_pocket = PocketFactory().create_pocket(
            pocket_id, wallet_id, pocket_type, pocket_name, amount
        )

        pocket_dict = {
            "pocket_id": new_pocket.pocket_id,
            "wallet_id": new_pocket.wallet_id,
            "type_": new_pocket.type_,
            "name": new_pocket.name,
            "amount": new_pocket.amount,
        }
        wallet.pockets.append(pocket_dict)

        self.repository.update_wallet(wallet)
        print(f"Pocket {new_pocket.name} created successfully")

    def show_pockets(self, wallet_id: str):
        """This method is used to show the pockets of a wallet."""
        wallet = self.get_walletid(wallet_id)
        return wallet.pockets

    def add_founds_pocket(self, wallet_id: str, pocket_id: str, amount: float):
        """This method is used to add funds to a pocket."""
        if amount <= 0:
            raise ValueError("The amount must be greater than 0")

        wallet = self.get_walletid(wallet_id)
        if amount > wallet.balance:
            raise ValueError("Insufficient balance")

        pocket = None
        for pocket in wallet.pockets:
            if pocket_id in pocket["pocket_id"]:
                pocket["amount"] += amount
                break

        self.repository.update_wallet(wallet)
        print(f"Founds added to pocket: {pocket}")

    def add_founds(self, wallet_id: str, amount: float):
        """This method is used to add funds to a wallet."""
        wallet = self.get_walletid(wallet_id)
        wallet.balance += amount
        self.repository.update_wallet(wallet)
        print(f"Founds added to wallet: {wallet}")
