from blockchain.block import Block
from blockchain.transaction import Transaction

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)

    def new_transaction(self, sender, recipient, contract_data):
        transaction = Transaction(sender, recipient, contract_data)
        self.current_transactions.append(transaction)
        return self.last_block.index + 1

    def new_block(self):
        block = Block(
            index=len(self.chain),
            transactions=[t.to_dict() for t in self.current_transactions],
            previous_hash=self.last_block.hash
        )
        self.current_transactions = []
        self.chain.append(block)
        return block

    @property
    def last_block(self):
        return self.chain[-1]

    def get_chain(self):
        return self.chain

    def query_blockchain(self, block_index=None):
        if block_index is not None:
            if 0 <= block_index < len(self.chain):
                return self.chain[block_index]
            else:
                return None
        else:
            return self.chain

