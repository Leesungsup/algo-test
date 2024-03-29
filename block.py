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


import hashlib
import time
import json
import ast

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
        self.current_transaction[hashlib.sha256(hex(len(self.current_transaction)).encode()).hexdigest()[:40]]={'sender' : sender, 'recipient' : recipient, 'amount' : amount, 'previoustransaction':hashlib.sha256(hex(len(self.current_transaction)-1).encode()).hexdigest()[:40]}
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

    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]

    def isValid(self):
        i = 1
        while(i<len(self.chain)):
            if(self.chain[i].hash != self.chain[i].calHash()):
                return False
            if(self.chain[i].previousHash != self.chain[i-1].hash):
                return False
            i += 1
        return True

    def istransactionValid(self):
        i=1
        while(i<len(self.chain[0].data)):
            print(hashlib.sha256(hex(i-1).encode()).hexdigest()[:40])
            print(self.chain[i].data[hashlib.sha256(hex(i).encode()).hexdigest()[:40]]["previoustransaction"])
            if(hashlib.sha256(hex(i-1).encode()).hexdigest()[:40] != self.chain[i].data[hashlib.sha256(hex(i).encode()).hexdigest()[:40]]["previoustransaction"]):
                return False
            i+=1
        return True

    def pow(self, last_proof):
        proof = 0
        print(last_proof)
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = str(last_proof + str(proof)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000" # nonce​

start = time.time()
newblockchain = BlockChain()
print(json.dumps(vars(newblockchain.chain[0]), indent=4))
newblockchain.addBlock(Block(len(newblockchain.chain),time.time(), {"sender":"h1","amount":4,"recipient":"h2"}))
for block in newblockchain.chain:
    print(json.dumps(vars(block), indent=4))
end = time.time()
last_block = newblockchain.last_block()
print("-------------------------------")
last_block=json.dumps(vars(last_block))
my_dict = ast.literal_eval(last_block)
print(my_dict)
print(my_dict['hash'])
last_hash = my_dict['hash']
proof = newblockchain.pow(last_hash)
print(proof)
print("===========================================")
print(newblockchain.istransactionValid())
print(f"{end - start:.5f} sec")

import hashlib
import time
import json
import ast

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
        self.current_transaction[hashlib.sha256(hex(len(self.current_transaction)).encode()).hexdigest()[:40]]={'sender' : sender, 'recipient' : recipient, 'amount' : amount, 'previoustransaction':hashlib.sha256(hex(len(self.current_transaction)-1).encode()).hexdigest()[:40]}
    def calHash(self):
        return hashlib.sha256(str(self.id).encode() + str(self.data).encode() + str(self.timestamp).encode() + str(self.previousHash).encode()).hexdigest()[:40]

class BlockChain:

    def __init__(self):
        self.chain = []
        self.powlist=[]
        #self.current_transactions = []
        self.createGenesis()

    def powvalid(self):
        k=0
        for block in self.chain:
            current_block=json.dumps(vars(block))
            my_dict = ast.literal_eval(current_block)
            hash = my_dict['hash']
            proof=self.pow(hash)
            self.powlist.append(proof)
        for i in range(len(self.chain)):
            current_block=json.dumps(vars(self.chain[i]))
            my_dict = ast.literal_eval(current_block)
            hash = my_dict['hash']
            if self.valid_proof(hash,self.powlist[i]) is False:
                k=1
                break
        if k==1:
            print("block이 잘못되었습니다.")
        else:
            print("block이 유효합니다.")
    def createGenesis(self):
        self.chain.append(Block(0, time.time(),  {"sender":"h1","amount":5,"recipient":"h2"}))

    def addBlock(self, nBlock):
        nBlock.previousHash = self.chain[len(self.chain)-1].hash
        nBlock.hash = nBlock.calHash()
        self.chain.append(nBlock)

    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]

    def isValid(self):
        i = 1
        while(i<len(self.chain)):
            if(self.chain[i].hash != self.chain[i].calHash()):
                return False
            if(self.chain[i].previousHash != self.chain[i-1].hash):
                return False
            i += 1
        return True

    def istransactionValid(self):
        i=1
        while(i<len(self.chain[0].data)):
            print(hashlib.sha256(hex(i-1).encode()).hexdigest()[:40])
            print(self.chain[i].data[hashlib.sha256(hex(i).encode()).hexdigest()[:40]]["previoustransaction"])
            if(hashlib.sha256(hex(i-1).encode()).hexdigest()[:40] != self.chain[i].data[hashlib.sha256(hex(i).encode()).hexdigest()[:40]]["previoustransaction"]):
                return False
            i+=1
        return True

    def pow(self, last_proof):
        proof = 0
        print(last_proof)
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = str(last_proof + str(proof)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000" # nonce​

start = time.time()
newblockchain = BlockChain()
print(json.dumps(vars(newblockchain.chain[0]), indent=4))
newblockchain.addBlock(Block(len(newblockchain.chain),time.time(), {"sender":"h1","amount":4,"recipient":"h2"}))
for block in newblockchain.chain:
    print(json.dumps(vars(block), indent=4))
end = time.time()
last_block = newblockchain.last_block()
print(last_block)
print("-------------------------------")
last_block=json.dumps(vars(last_block))
my_dict = ast.literal_eval(last_block)
print(my_dict)
print(my_dict['hash'])
last_hash = my_dict['hash']
proof = newblockchain.pow(last_hash)
print(proof)
print("===========================================")
#print(newblockchain.istransactionValid())
print(newblockchain.powvalid())
print(newblockchain.powlist)
print(f"{end - start:.5f} sec")
