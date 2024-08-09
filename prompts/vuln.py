# prompts/vuln.py

from prompts.core import BasePromptTemplate

__all__ = ["VulnerabilityTemplate"]

class VulnerabilityTemplate(BasePromptTemplate):
    """Vulnerability Analysis Template for smart contracts."""
    
    def __init__(self, template: str = None):
        if template is None:
            template = """
            Analyze the following smart contract for security vulnerabilities:
            $contract_code

            Provide a detailed analysis and recommendations for improvement.
            """
        super().__init__(template)

    def format(self, **kwds) -> str:
        return super().format(**kwds)

