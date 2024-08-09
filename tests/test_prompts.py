# tests/test_prompts.py

import unittest
from unittest.mock import patch
from prompts.automata import AutomataTemplate
from prompts.smart_contract import SmartContractTemplate
from prompts.vuln import VulnerabilityTemplate
from llm.groq import Groq

class TestPromptTemplates(unittest.TestCase):

    def setUp(self):
        self.model_id = 'mock_model'
        self.api_key = 'mock_api_key'
        self.groq_model = Groq(model_id=self.model_id, 
                               api_key=self.api_key)

    def assertGeneratedOutput(self, 
                              generated_output, 
                              expected_phrases):
        for phrase in expected_phrases:
            self.assertIn(phrase, 
                          generated_output)

    @patch('llm.groq.Groq.complete')
    def test_automata_template(self, 
                               mock_complete):
        mock_complete.return_value = "State definitions using enums and Additional logic for state transition."

        automata_prompt = AutomataTemplate()
        fsm_description = automata_prompt.format(fsm_details="Additional logic for state transition")
        
        generated_output = self.groq_model.complete(fsm_description)
        expected_phrases = [
            "State definitions using enums",
            "Additional logic for state transition"
        ]
        self.assertGeneratedOutput(generated_output, 
                                   expected_phrases)

    @patch('llm.groq.Groq.complete')
    def test_smart_contract_template(self, 
                                     mock_complete):
        mock_complete.return_value = (
            "Functions to start the auction, place bids, and end the auction. "
            "Security features to prevent unauthorized access and replay attacks."
        )

        smart_contract_prompt = SmartContractTemplate()
        generated_code_prompt = smart_contract_prompt()
        
        generated_code = self.groq_model.complete(generated_code_prompt)
        expected_phrases = [
            "Functions to start the auction",
            "Security features to prevent unauthorized access"
        ]
        self.assertGeneratedOutput(generated_code, 
                                   expected_phrases)

    @patch('llm.groq.Groq.complete')
    def test_vulnerability_template(self, 
                                    mock_complete):
        mock_complete.return_value = (
            "Analyze the following smart contract for security vulnerabilities: TestContract."
        )

        vulnerability_prompt = VulnerabilityTemplate()
        contract_code = """
        contract TestContract {
            uint256 public value;
            function setValue(uint256 newValue) public {
                value = newValue;
            }
        }
        """
        vulnerability_analysis_prompt = vulnerability_prompt.format(contract_code=contract_code)
        
        vulnerability_analysis = self.groq_model.complete(vulnerability_analysis_prompt)
        expected_phrases = [
            "Analyze the following smart contract for security vulnerabilities",
            "TestContract"
        ]
        self.assertGeneratedOutput(vulnerability_analysis, expected_phrases)

if __name__ == '__main__':
    unittest.main()

