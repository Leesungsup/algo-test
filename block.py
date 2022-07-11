import hashlib
import time
import json

class Block():
    current_transaction = dict()
    def __init__(self, id, timestamp, data):
        self.new_transaction(data["sender"],data["recipient"],data["amount"])
        self.id = hex(id)
        self.timestamp = timestamp
        self.data = self.current_transaction
        self.previousHash = 0
        self.hash = self.calHash()
    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the list of transaction
        self.current_transaction[hashlib.sha256(hex(len(self.current_transaction)).encode()).hexdigest()[:40]]={'sender' : sender, 'recipient' : recipient, 'amount' : amount}
    def calHash(self):
        return hashlib.sha256(str(self.id).encode() + str(self.data).encode() + str(self.timestamp).encode() + str(self.previousHash).encode()).hexdigest()[:40]

class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.createGenesis()

    def createGenesis(self):
        self.chain.append(Block(0, time.time(),  {"sender":"h1","amount":5,"recipient":"h2"}))

    def addBlock(self, nBlock):
        nBlock.previousHash = self.chain[len(self.chain)-1].hash
        nBlock.hash = nBlock.calHash()
        self.chain.append(nBlock)

    def isValid(self):
        i = 1
        while(i<len(self.chain)):
            if(self.chain[i].hash != self.chain[i].calHash()):
                return False
            if(self.chain[i].previousHash != self.chain[i-1].hash):
                return False
            i += 1
        return True

onion = BlockChain()
print(json.dumps(vars(onion.chain[0]), indent=4))
data={"sender":"h1","amount":4,"recipient":"h2"}
print(data["sender"],data["amount"],data["recipient"])
onion.addBlock(Block(len(onion.chain),time.time(), {"sender":"h1","amount":4,"recipient":"h2"}))
for block in onion.chain:
    print(json.dumps(vars(block), indent=4))
