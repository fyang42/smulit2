# prompts/legal/employment_contract.py

# referenced from https://www.mom.gov.sg/employment-practices/contract-of-service/what-is-a-contract-of-service#:~:text=The%20contract%20must%20include%20key,the%20employer%20as%20an%20employee


from prompts.core import BasePromptTemplate

__all__ = ["EmploymentContractTemplate"]

class EmploymentContractTemplate(BasePromptTemplate):
    """Smart Contract Template for generating an Employment Contract with Key Employment Terms (KETs) and essential clauses."""
    
    def __init__(self):
        template = """
        Generate a Solidity smart contract for an Employment Contract with the following features:
        
        1. Definitions of Employer and Employee roles, including a clear agreement that one person agrees to employ another as an employee, and the other agrees to serve the employer as an employee.
        
        2. Basic terms of employment, including salary, job title, responsibilities, and work arrangements. Ensure that the contract includes all required Key Employment Terms (KETs) as listed below:
        
        Key Employment Terms (KETs):
        1. Full name of employer.
        2. Full name of employee.
        3. Job title, main duties, and responsibilities.
        4. Start date of employment.
        5. Duration of employment (if employee is on a fixed-term contract).
        6. Working arrangements, such as:
           - Daily working hours (e.g., 8:30 am – 6:00 pm).
           - Number of working days per week (e.g., six).
           - Rest day (e.g., Saturday).
        7. Salary period.
        8. Basic salary, including the rate of pay for hourly, daily, or piece-rated workers.
        9. Fixed allowances.
        10. Fixed deductions.
        11. Overtime payment period (if different from salary period).
        12. Overtime rate of pay.
        13. Other salary-related components, such as bonuses and incentives.
        14. Type of leave (e.g., annual leave, outpatient sick leave, hospitalization leave, maternity leave, childcare leave).
        15. Other medical benefits (e.g., insurance, medical benefits, dental benefits).
        16. Probation period.
        17. Notice period.
        18. Place of work (optional, but recommended if different from the employer’s address).

        3. Performance-based bonus system, including criteria for bonuses and calculation methods.
        
        4. Payment schedule for salary and bonuses, including mechanisms to verify compliance with agreed-upon terms.
        
        5. Termination clauses, including reasons for termination, notice periods, and conditions under which termination can occur.
        
        6. Confidentiality and non-compete clauses, as well as other relevant clauses that might apply to the specific employment scenario.
        
        7. Dispute resolution mechanisms, including arbitration or mediation, as well as specific references to relevant acts (e.g., Employment Claims Act) where applicable.
        
        8. Constructor function to initialize the contract with the relevant parties and terms, ensuring that all essential clauses are clearly defined and agreed upon by both parties.
        
        9. Additional clauses to distinguish between contracts of service and contracts for service, including control, ownership of factors of production, and economic considerations.
        """
        super().__init__(template)

    def format(self, **kwds) -> str:
        return super().format(**kwds)
