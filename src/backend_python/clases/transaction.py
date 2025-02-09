"""This file is a module that contains the Transaction class."""

from pydantic import BaseModel

class Transaction(BaseModel):
    """This class is a model that represents a transaction."""
    id_reference: str
    wallet_id: str
    amount: float
    date: str
    where_to: str

    @staticmethod
    def add_transaction(wallet_id: str):
        """This method adds a transaction."""
