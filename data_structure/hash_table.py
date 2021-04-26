class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
class HashTable:
    def __init__(self, table_size):
        self.table_size = table_size
        self.hash_table = [None] * table_size
        
    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i)
            # print(f'1: {hash_value}')
            hash_value = (hash_value * ord(i)) % self.table_size
            # print(f'2: {hash_value}')
        return hash_value
    
    def add_key_value(self, key, value):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            self.hash_table[hashed_key] = Node(Data(key, value), None)
        else:
            node = self.hash_table[hashed_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key, value), None)
            
    def get_value(self, key):
        hashed_key = self.custom_hash(key)
        if self.hash_table[hashed_key] is None:
            raise AttributeError('no node mapped')
        
        node = self.hash_table[hashed_key]
        while node.next_node:
            if key == node.data.key:
                return node.data.value
            node = node.next_node
        if key == node.data.key:
            return node.data.key
        raise AttributeError('No node with the key')
    
    def print_table(self):
        print("{")
        for i, node in enumerate(self.hash_table):
            if node is not None:
                ll_string = ""
                while node.next_node:
                    node_string = f"{node.data.key} : {node.data.value}"
                    ll_string += (node_string + " --> ")
                    node = node.next_node
                node_string = f"{node.data.key} : {node.data.value}"
                ll_string += (node_string + " --> None")
                print(f"\t[{i}]" + ll_string)
            else:
                print(f"\t[{i}] {node}")
        print("}")
                    
ht = HashTable(3)                       
ht.add_key_value('apple', 'iphone')
ht.add_key_value('samsung', 's21')
ht.add_key_value('one', 'two')
ht.add_key_value('hi', 'there')
ht.add_key_value('hello', 'world')
ht.add_key_value('python', 'pythonista')
                
                    
        
        