
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Bintree:
    def __init__(self):
        self.root = None

    def put(self,newvalue):

        self.root = putta(self.root, newvalue)
        
    def __contains__(self,newvalue):
        
        return finns(self.root, newvalue)
        
    def write(self):
        
        skriv(self.root)
        print("\n")

    def size(self):
        return antal(self.root)
            


def finns(root, newvalue):

    if not root:
        return False
    
    if newvalue == root.value:
        
        return True
    
    if root.value > newvalue:
        return finns(root.left, newvalue)

    if root.value < newvalue:
        return finns(root.right, newvalue)

def putta(root, newvalue):
    
    new_node = Node(newvalue)
    
    if root is None:
        root = new_node
    else:
        if newvalue < root.value:
            if root.left is None:
                root.left = new_node
            else:
                putta(root.left, newvalue)
            
        if newvalue > root.value:
            if root.right is None:
                root.right = new_node
            else:
                putta(root.right, newvalue)
        if newvalue == root.value:
            root = root
    return root
    
def skriv(root):
    
    if root != None:
        skriv(root.left)
        print(root.value)
        skriv(root.right)

def antal(root):
        if root == None: 
            return 0
        else:
            return 1 + antal(root.left) + antal(root.right)
