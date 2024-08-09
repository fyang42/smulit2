# prompts/legal/__init__.py

from prompts.legal.escrow_service import EscrowServiceTemplate
from prompts.legal.employment_contract import EmploymentContractTemplate
from prompts.legal.nda import NDATemplate
from prompts.legal.rental_agreement import RentalAgreementTemplate
from prompts.legal.secure_data_management import SecureDataManagementTemplate

__all__ = [
    "EscrowServiceTemplate",
    "EmploymentContractTemplate",
    "NDATemplate",
    "RentalAgreementTemplate",
    "SecureDataManagementTemplate"
]
