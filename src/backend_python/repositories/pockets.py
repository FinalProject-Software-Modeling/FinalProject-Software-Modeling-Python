"""This file is a module that contains the pockets class"""

from pydantic import BaseModel

class PocketDao(BaseModel):
    """This class is used to define data structure related to pockets."""
    pocket_id: str
    wallet_id: str
    type_: str
    name: str
    amount: float

class PocketBills(PocketDao):
    """This class is used to define data structure related to bills pockets."""

class PocketSavings(PocketDao):
    """This class is used to define data structure related to savings pockets."""

class PocketInvestments(PocketDao):
    """This class is used to define data structure related to investments pockets."""
