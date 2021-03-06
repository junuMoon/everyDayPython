class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        
    def to_list(self):
        l = []
        if self.head is None:
            return l
        else:
            node = self.head
            while node:
                l.append(node.data)
                node = node.next_node
            return l
        
    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} -> "
            node = node.next_node
        ll_string += "None"
        print(ll_string)
        
    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        else:
            new_node = Node(data, self.head)
            self.head = new_node
        
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node
        
    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] == int(user_id):
                return node.data
            node = node.next_node
        raise AttributeError('user not found')
    
ll = LinkedList()
ll.insert_beginning({
        "address": "5-103",
        "email": "junu@email.com",
        "id": 1,
        "name": "Junu",
        "phone": "0109312332"
    })
ll.insert_beginning({
        "address": "72832 Jones Plains Apt. 342\nWest Dustinville, WA 23799",
        "email": "Teresa_Taylor@email.com",
        "id": 2,
        "name": "Teresa Taylor",
        "phone": "3139418534977"
    })
ll.insert_beginning({
        "address": "752 Elliott Corners\nMasseyport, DC 79245",
        "email": "Mrs._Kimberly_Cross_MD@email.com",
        "id": 3,
        "name": "Mrs. Kimberly Cross MD",
        "phone": "2574061753767"
    })
# ll.insert_beginning('data4')