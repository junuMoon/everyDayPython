import hashlib
import json
from time import time
import uuid


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        
    def new_block(self, proof, previous_hash=None):
        # Creates a new Block and adds it to the chain
        """
        Create a new block in the Blockchain
        
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block()),
        }
        
        self.current_transactions = []
        
        self.chain.append(block)
        
        return block
    
    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions
        
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        
        return self.last_block['index'] +1
    
    def proof_of_work(self, last_proof):
        """Simple Proof of Work Algorithm:
        - Find a numper p' such that hash(pp') contains leading 4 zeros, where p is the previous p'
        - p is the previous proof, and p' is the new proof

        Args:
            last_proof (int): last proof of work

        Returns:
            proof (int): new proof of work
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
            
        return proof
        
    @staticmethod
    def valid_proof(last_proof, proof):
        """Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeros?

        Args:
            last_proof (int): Previous proof
            proof (int): current proof

        Returns:
            (bool): True if correct
        """
        
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
    
    @staticmethod
    def hash(block):
        """
        Create a SHA-256 has of a Block
        
        :param block: <dict> Block
        :return: <str>
        """
        
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    @property
    def last_block(self):
        # Returns the las block in the chain
        return self.chain[-1]
    
    