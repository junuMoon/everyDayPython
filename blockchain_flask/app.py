import json
from flask import Flask, request, render_template
import uuid

from blockchain import Blockchain


# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid.uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/', methods=['GET'])
def home():
    return render_template('/home.html')


@app.route('/mine', methods=['GET'])
def mine():
    # We run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    
    # We must receive a reward for finding the proof
    # The sender is "0" to signify that this node has mined a new coin.
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1
    )
    
    # Forge the new Vblock by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)
    
    response = {
        'message': "새로운 블락 생성",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return json.dumps(response)

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    
    # Check that the required fields are in the POSTed data
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing Values', 400
    
    # Create a new Transaction
    index = blockchain.new_transaction(
                values['sender'],
                values['recipient'],
                values['amount']
            )
    
    response = {
        'message': f'Transaction will be added to Block {index}',
        }
    return json.dumps(response)

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return json.dumps(response)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)