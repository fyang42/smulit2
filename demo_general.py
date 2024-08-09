import os
from dotenv import load_dotenv
from prompts.automata import AutomataTemplate
from prompts.smart_contract import SmartContractTemplate
from prompts.vuln import VulnerabilityTemplate
from llm.groq import Groq

# Load environment variables
load_dotenv()

API_KEY = os.getenv('GROQ_API_KEY')
MODEL_ID = os.getenv('GROQ_MODEL_ID')

def generate_output(llm, 
                    template_class, 
                    description=None):
    prompt_instance = template_class()
    if description:
        prompt = prompt_instance.format(fsm_details=description)
    else:
        prompt = prompt_instance()
    return llm.complete(prompt)

def demo():
    # Initialize the Groq LLM
    llm = Groq(model_id=MODEL_ID, 
               api_key=API_KEY)

    # Define templates and their descriptions (if applicable)
    templates = [
        (AutomataTemplate, "Additional logic for state transition", "FSM Description"),
        (SmartContractTemplate, None, "Generated Smart Contract"),
        (VulnerabilityTemplate, """
            contract DemoContract {
                uint256 public value;
                function setValue(uint256 newValue) public {
                    value = newValue;
                }
            }
            """, "Vulnerability Analysis")
    ]

    # Generate and display outputs
    for template_class, description, output_label in templates:
        output = generate_output(llm, 
                                 template_class, 
                                 description)
        print(f"\n{output_label}:\n", output)

if __name__ == "__main__":
    demo()
