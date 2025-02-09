"""This file is a module that contains the Pocket class."""

from pydantic import BaseModel

class Pocket(BaseModel):
    """This class is a model that represents a pocket."""
    id: str
    wallet_id: str
    name: str
    amount: str

class PocketBills(Pocket):
    """This class is a model that represents a pocket with bills."""
    bills: dict
    date: str

class PocketSavings(Pocket):
    """This class is a model that represents a pocket with savings."""
    goal: str
    date: str
    interest: str

class PocketInvestment(Pocket):
    """This class is a model that represents a pocket with investments."""
    period_time: str
    interest: str
