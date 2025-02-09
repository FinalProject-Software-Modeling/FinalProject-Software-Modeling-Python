"""This module has a class to handle enviroment variables into the application."""

import os
from dotenv import load_dotenv

load_dotenv()

class EnvironmentVariables():
    """This class is used to handle environment variables."""
    
    def __init__(self):
        """This method initializes the class."""
        self.wallets_data = os.getenv("WALLETS_DATA")
