"""This module is used to fdefine the factory pockets."""

from repositories.pockets import PocketBills, PocketSavings, PocketInvestments


class PocketFactory:
    """This class is used to create pockets."""

    @staticmethod
    def create_pocket(
        pocket_id: str, wallet_id: str, type_: str, name: str, amount: float
    ):
        """This method is used to create a pocket."""
        type_ = type_.lower()
        if type_ == "bills":
            return PocketBills(
                pocket_id=pocket_id,
                wallet_id=wallet_id,
                type_=type_,
                name=name,
                amount=amount,
            )
        elif type_ == "savings":
            return PocketSavings(
                pocket_id=pocket_id,
                wallet_id=wallet_id,
                type_=type_,
                name=name,
                amount=amount,
            )
        elif type_ == "investments":
            return PocketInvestments(
                pocket_id=pocket_id,
                wallet_id=wallet_id,
                type_=type_,
                name=name,
                amount=amount,
            )
        else:
            raise ValueError("Invalid pocket type")
