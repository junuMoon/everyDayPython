class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def _insert_recursive(self, data, node):
        if data["id"] < node.data["id"]:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        elif data["id"] > node.data["id"]:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)
        else:
            return
        
    def _search_recursive(self, id, node):
        try:
            if id == node.data["id"]:
                return node.data
            elif id < node.data["id"]:
                return self._search_recursive(id, node.left)
            else:
                return self._search_recursive(id, node.right)
        except AttributeError as e:
            return False
            
    def search(self, blog_post_id):
        blog_post_id = int(blog_post_id)
        if self.root is None:
            raise AttributeError('no root')
        else:
            return self._search_recursive(blog_post_id, self.root)
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)
        
# def depth_counter(func):
#     depth_counter.depth = 0
#     def wrapper(*args, **kwargs):
#         depth_counter.depth += 1
#         result = func(*args, **kwargs)
#         return result
