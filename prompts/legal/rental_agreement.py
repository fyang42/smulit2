# prompts/legal/rental_agreement.py

from prompts.core import BasePromptTemplate

__all__ = ["RentalAgreementTemplate"]

class RentalAgreementTemplate(BasePromptTemplate):
    """Smart Contract Template for generating a Rental Agreement for Property Leasing."""
    
    def __init__(self):
        template = """
        Generate a Solidity smart contract for a Rental Agreement with the following features:
        1. Definitions of the Lessor (property owner) and Lessee (tenant).
        2. Description of the leased property and rental terms.
        3. Payment schedule for rent, including late fees and penalties for non-payment.
        4. Security deposit handling, including conditions for its return.
        5. Maintenance and repair obligations of both parties.
        6. Termination and renewal clauses, including notice periods.
        7. Dispute resolution mechanisms, including arbitration or mediation.
        8. Constructor function to initialize the contract with the relevant parties and terms.
        """
        super().__init__(template)

    def format(self, **kwds) -> str:
        return super().format(**kwds)
