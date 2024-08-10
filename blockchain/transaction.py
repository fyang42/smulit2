import uuid

class Transaction:
    def __init__(self, sender, recipient, contract_data):
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.contract_data = contract_data

    def to_dict(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'recipient': self.recipient,
            'contract_data': self.contract_data
        }
