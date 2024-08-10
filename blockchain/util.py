import hashlib

def hash_block(block_string):
    return hashlib.sha256(block_string.encode()).hexdigest()
