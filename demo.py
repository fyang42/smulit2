# demo.py

import os
from dotenv import load_dotenv
from prompts.automata import AutomataTemplate
from prompts.smart_contract import SmartContractTemplate
from prompts.vuln import VulnerabilityTemplate
from llm.groq import Groq

# Load environment variables
load_dotenv()

API_KEY = os.getenv('GROQ_API_KEY')
MODEL_ID = 'mixtral-8x7b-32768'

def demo():
    # Initialize the Groq LLM
    llm = Groq(model_id=MODEL_ID, 
               api_key=API_KEY)

    # Automata Template Demo
    automata_prompt = AutomataTemplate()
    fsm_description = automata_prompt.format(fsm_details="Additional logic for state transition")
    fsm_output = llm.complete(fsm_description)
    print("FSM Description:\n", fsm_output)
    
    # Smart Contract Template Demo
    smart_contract_prompt = SmartContractTemplate()
    generated_code_prompt = smart_contract_prompt()
    generated_code = llm.complete(generated_code_prompt)
    print("\nGenerated Smart Contract:\n", generated_code)
    
    # Vulnerability Template Demo
    vulnerability_prompt = VulnerabilityTemplate()
    contract_code = """
    contract DemoContract {
        uint256 public value;
        function setValue(uint256 newValue) public {
            value = newValue;
        }
    }
    """
    vulnerability_analysis_prompt = vulnerability_prompt.format(contract_code=contract_code)
    vulnerability_analysis = llm.complete(vulnerability_analysis_prompt)
    print("\nVulnerability Analysis:\n", vulnerability_analysis)

if __name__ == "__main__":
    demo()
