# prompts/legal/nda.py

from prompts.core import BasePromptTemplate

__all__ = ["NDATemplate"]

class NDATemplate(BasePromptTemplate):
    """Smart Contract Template for generating a Non-Disclosure Agreement (NDA)."""
    
    def __init__(self):
        template = """
        Generate a Solidity smart contract for a Non-Disclosure Agreement (NDA) with the following features:
        1. Definitions of Confidential Information and Parties involved (Discloser and Recipient).
        2. Obligations of the Recipient to maintain confidentiality.
        3. Duration of the confidentiality obligation.
        4. Permitted disclosures and exceptions (e.g., legal requirements).
        5. Consequences for breach of the NDA, including potential penalties.
        6. Dispute resolution mechanisms, including arbitration or mediation.
        7. Constructor function to initialize the contract with the relevant parties and terms.
        """
        super().__init__(template)

    def format(self, **kwds) -> str:
        return super().format(**kwds)
