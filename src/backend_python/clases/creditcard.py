"""This file is a module that contains the Credit_card class."""
from pydantic import BaseModel

class CreditCard(BaseModel):
    """This class is a model that represents a credit card."""
    wallet_id: str
    card_number: str
    due_date: str
    cvv: str
    card_holder: str
