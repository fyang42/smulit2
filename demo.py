# demo.py

from prompts.automata import AutomataTemplate
from prompts.smart_contract import SmartContractTemplate
from prompts.vuln import VulnerabilityTemplate

def demo():
    # Automata Template Demo
    automata_prompt = AutomataTemplate()
    fsm_description = automata_prompt.format(fsm_details="Additional logic for state transition")
    print("FSM Description:\n", fsm_description)
    
    # Smart Contract Template Demo
    smart_contract_prompt = SmartContractTemplate()
    generated_code = smart_contract_prompt()
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
    vulnerability_analysis = vulnerability_prompt(contract_code=contract_code)
    print("\nVulnerability Analysis:\n", vulnerability_analysis)

if __name__ == "__main__":
    demo()
