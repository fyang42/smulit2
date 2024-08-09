# prompts/__init__.py

from prompts.core import (
    AbstractPromptTemplate,
    BasePromptTemplate,
    BaseConversationTemplate,
)
from prompts.smart_contract import SmartContractTemplate
from prompts.automata import AutomataTemplate
from prompts.vuln import VulnerabilityTemplate
from prompts.legal import *

__all__ = [
    "AbstractPromptTemplate",
    "BasePromptTemplate",
    "BaseConversationTemplate",
    "SmartContractTemplate",
    "AutomataTemplate",
    "VulnerabilityTemplate",
    "EscrowServiceTemplate",
    "EmploymentContractTemplate",
    "NDATemplate",
    "RentalAgreementTemplate",
    "SecureDataManagementTemplate"
]
