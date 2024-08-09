# prompts/smart_contract.py

from prompts.core import BasePromptTemplate

__all__ = ["SmartContractTemplate"]

class SmartContractTemplate(BasePromptTemplate):
    """Smart Contract Template for generating Solidity contracts."""
    
    def __init__(self):
        template = """
        Generate a Solidity smart contract with the following features:
        1. Functions to start the auction, place bids, and end the auction.
        2. Security features to prevent unauthorized access and replay attacks.
        3. Proper handling of Ether deposits and withdrawals.
        """
        super().__init__(template)

    def format(self, **kwds) -> str:
        return super().format(**kwds)
