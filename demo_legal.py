# demo_legal.py

import os
import tkinter as tk
import threading

from dotenv import load_dotenv
from tkinter import simpledialog, messagebox, scrolledtext
from prompts.legal.escrow_service import EscrowServiceTemplate
from prompts.legal.employment_contract import EmploymentContractTemplate
from prompts.legal.nda import NDATemplate
from prompts.legal.rental_agreement import RentalAgreementTemplate
from prompts.legal.secure_data_management import SecureDataManagementTemplate
from llm.groq import Groq
from blockchain import Blockchain

load_dotenv()

API_KEY = os.getenv('GROQ_API_KEY')
MODEL_ID = os.getenv('GROQ_MODEL_ID')

def get_contract_options():
    return {
        'escrow service': EscrowServiceTemplate,
        'employment contract': EmploymentContractTemplate,
        'nda contract': NDATemplate,
        'rental agreement': RentalAgreementTemplate,
        'secure data management': SecureDataManagementTemplate
    }

def get_user_selection(contract_options):
    root = tk.Tk()
    root.withdraw()
    contract_names = list(contract_options.keys())
    selected_contract = simpledialog.askstring(
        "Contract Selection", 
        f"Please select a contract type:\n{', '.join(contract_names)}"
    )
    root.destroy()

    if selected_contract is None:
        return None

    selected_contract = selected_contract.strip().lower()

    if selected_contract in contract_options:
        return selected_contract
    else:
        messagebox.showerror("Error", "Invalid selection. Please choose a valid contract type.")
        return get_user_selection(contract_options)

def collect_contract_details(contract_name):
    details = {}
    root = tk.Tk()
    root.withdraw()
    input_prompts = {
        'escrow service': [
            ("buyer", "Enter the Buyer’s address:"),
            ("seller", "Enter the Seller’s address:"),
            ("escrow_agent", "Enter the Escrow Agent’s address:")
        ],
        'employment contract': [
            ("employer", "Enter the Employer's name:"),
            ("employee", "Enter the Employee's name:"),
            ("salary", "Enter the Salary amount:"),
            ("job_title", "Enter the Job Title:")
        ],
        'nda contract': [
            ("discloser", "Enter the Discloser’s name:"),
            ("recipient", "Enter the Recipient’s name:"),
            ("duration", "Enter the duration of confidentiality:")
        ],
        'rental agreement': [
            ("lessor", "Enter the Lessor's name:"),
            ("lessee", "Enter the Lessee's name:"),
            ("property", "Enter the Property description:"),
            ("rent_amount", "Enter the Rent amount:")
        ],
        'secure data management': [
            ("data_owner", "Enter the Data Owner's name:"),
            ("authorized_users", "Enter the list of authorized users (comma-separated):"),
            ("encryption_method", "Enter the encryption method (e.g., AES-256):"),
            ("access_policies", "Describe the access policies:"),
            ("audit_policies", "Describe the audit policies:"),
        ]
    }

    for key, prompt in input_prompts.get(contract_name, []):
        details[key] = simpledialog.askstring("Input", prompt)
    root.destroy()
    return details

def generate_contract(llm, 
                      template_class, 
                      details, timeout=60):
    prompt_instance = template_class()
    contract_prompt = prompt_instance.format(**details)
    
    result = []
    def run_llm():
        result.append(llm.complete(contract_prompt))

    llm_thread = threading.Thread(target=run_llm)
    llm_thread.start()
    llm_thread.join(timeout)

    if llm_thread.is_alive():
        messagebox.showerror("Timeout", 
                             "The contract generation process took too long and was terminated.")
        return "Contract generation timed out."
    else:
        return result[0]

def save_contract_to_file(contract_name, contract_data):
    filename = f"{contract_name.replace(' ', '_')}_contract.txt"
    with open(filename, 'w') as file:
        file.write(contract_data)
    return filename

def upload_contract_to_blockchain(contract_name, contract_data, blockchain):
    transaction_index = blockchain.new_transaction(
        sender="user_wallet_address",  # Placeholder for a real user wallet address
        recipient="contract_deployment_address",  # Placeholder for the deployment address
        contract_data=contract_data
    )
    
    block = blockchain.new_block()
    
    log_message = (
        f"Contract '{contract_name}' uploaded to the blockchain.\n"
        f"Transaction Index: {transaction_index}\n"
        f"Block Index: {block.index}\n"
        f"Previous Hash: {block.previous_hash}\n"
        f"Block Hash: {block.hash}\n"
        f"Transactions in Block: {len(block.transactions)}\n"
        f"Timestamp: {block.timestamp}\n"
    )
    
    filename = f"{contract_name.replace(' ', '_')}_contract.txt"
    with open(filename, 'a') as file:
        file.write("\n" + log_message + "\n")

    messagebox.showinfo("Blockchain Upload", log_message)

def query_blockchain_logs(blockchain):
    root = tk.Tk()
    root.title("Blockchain Query Results")

    blocks = blockchain.get_chain()
    listbox = tk.Listbox(root, width=120, height=20)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(root)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    for block in blocks:
        listbox.insert(tk.END, f"Block Index: {block.index}, Block Hash: {block.hash[:8]}...")

    def on_block_select(event):
        selected_index = listbox.curselection()
        if selected_index:
            selected_block = blocks[selected_index[0]]
            display_contract_details(selected_block)

    listbox.bind("<<ListboxSelect>>", on_block_select)
    scrollbar.config(command=listbox.yview)

    root.mainloop()

def display_contract_details(block):
    root = tk.Tk()
    root.title(f"Block Index: {block.index} Details")

    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=120, height=40)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    transactions_text = "\n".join([
        f" Sender: {tx['sender']}\n Recipient: {tx['recipient']}\n Contract Data: {tx['contract_data']}\n"
        for tx in block.transactions
    ])
    
    text_area.insert(tk.END, f"Block Index: {block.index}\n")
    text_area.insert(tk.END, f"Previous Hash: {block.previous_hash}\n")
    text_area.insert(tk.END, f"Block Hash: {block.hash}\n")
    text_area.insert(tk.END, f"Timestamp: {block.timestamp}\n")
    text_area.insert(tk.END, f"Transactions:\n{transactions_text}\n")

    root.mainloop()

def display_contract_output(contract_name, output_data, blockchain):
    save_contract_to_file(contract_name, output_data)
    upload_contract_to_blockchain(contract_name, output_data, blockchain)

def query_blockchain_option(blockchain):
    root = tk.Tk()
    root.withdraw()
    query_choice = messagebox.askyesno("Query Blockchain", "Would you like to query the blockchain logs now?")
    root.destroy()

    if query_choice:
        query_blockchain_logs(blockchain)

def main():
    llm = Groq(model_id=MODEL_ID, api_key=API_KEY)
    blockchain = Blockchain()

    contract_options = get_contract_options()
    selected_contract = get_user_selection(contract_options)

    if selected_contract:
        details = collect_contract_details(selected_contract)
        messagebox.showinfo("Processing", "Generating contract. Please wait...")
        generated_contract = generate_contract(llm, 
                                               contract_options[selected_contract], 
                                               details)
        display_contract_output(selected_contract, generated_contract, blockchain)
        query_blockchain_option(blockchain)
    else:
        messagebox.showerror("Error", "No contract type selected.")

if __name__ == "__main__":
    main()
