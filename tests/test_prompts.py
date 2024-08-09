# tests/test_prompts.py

import unittest
from prompts.automata import AutomataTemplate
from prompts.smart_contract import SmartContractTemplate
from prompts.vuln import VulnerabilityTemplate

class TestPromptTemplates(unittest.TestCase):

    def test_automata_template(self):
        automata_prompt = AutomataTemplate()
        fsm_description = automata_prompt.format(fsm_details="Additional logic for state transition")
        self.assertIn("State definitions using enums", fsm_description)
        self.assertIn("Additional logic for state transition", fsm_description)

    def test_smart_contract_template(self):
        smart_contract_prompt = SmartContractTemplate()
        generated_code = smart_contract_prompt()
        self.assertIn("Functions to start the auction", generated_code)
        self.assertIn("Security features to prevent unauthorized access", generated_code)

    def test_vulnerability_template(self):
        vulnerability_prompt = VulnerabilityTemplate()
        contract_code = """
        contract TestContract {
            uint256 public value;
            function setValue(uint256 newValue) public {
                value = newValue;
            }
        }
        """
        vulnerability_analysis = vulnerability_prompt(contract_code=contract_code)
        self.assertIn("Analyze the following smart contract for security vulnerabilities", vulnerability_analysis)
        self.assertIn("TestContract", vulnerability_analysis)

if __name__ == '__main__':
    unittest.main()
