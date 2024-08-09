# prompts/automata.py

from prompts.core import BasePromptTemplate

__all__ = ["AutomataTemplate"]

class AutomataTemplate(BasePromptTemplate):
    """Automata Template for defining state machines in smart contracts."""
    
    def __init__(self):
        template = """
        Describe how a Finite State Machine (FSM) can be implemented in a smart contract.
        Include the following:
        1. State definitions using enums.
        2. Transition functions between states.
        3. Guards and actions associated with each transition.

        Additional details to include: "$fsm_details"
        """
        super().__init__(template)

    def format(self, **kwds) -> str:
        return super().format(**kwds)
