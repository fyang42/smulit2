# prompts/legal/escrow_service.py

from prompts.core import BasePromptTemplate

__all__ = ["EscrowServiceTemplate"]

class EscrowServiceTemplate(BasePromptTemplate):
    """Smart Contract Template for generating an Escrow Service Agreement."""
    
    def __init__(self):
        template = """
        Generate a Solidity smart contract for an Escrow Service with the following features:
        1. Definitions of the Buyer, Seller, and Escrow Agent roles.
        2. Mechanism for depositing funds into escrow by the Buyer.
        3. Conditions for the release of funds to the Seller, such as delivery confirmation or mutual agreement.
        4. Procedure for resolving disputes, including the role of the Escrow Agent in mediating and deciding outcomes.
        5. Handling of refunds to the Buyer in case of contract cancellation or unmet conditions.
        6. Event logging for all major actions, such as deposits, releases, and disputes.
        7. Security features to prevent unauthorized access or tampering.
        8. Constructor function to initialize the contract with the relevant parties and terms.
        """
        super().__init__(template)

    def format(self, **kwds) -> str:
        return super().format(**kwds)
