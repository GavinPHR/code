
class AVL:

    def __init__(self, key: int = None, val: str = None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def find(self, key: int):
        node = self
        while node != None and node.key != key:
            if key < node.key: node =  node.left
            else: node = node.right
        if node != None and node.key == key: return node.val
        else: return ""
