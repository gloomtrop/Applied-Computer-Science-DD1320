from collections import Counter
import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.level = None
        self.parent = None
        self.balanced = True
        self.matches = 0
        
        if value.isnumeric():
            self.sum = int(value)

        def __eq__(self, other): 
            if not isinstance(other, Node):
                # don't attempt to compare against unrelated types
                return NotImplemented

            return self.value == other.value and self.left == other.left and self.right == other.right and self.balanced == other.balanced and self.parent == other.parent

class Tree:
    def __init__(self):
        self.root = None
        self.leaves = []
        self.leavecount = 0

    def put(self, newvalue):
        level = 0
        leaves = []
        self.root, self.leaves, self.leavecount = putta(self.root, newvalue, level, self.leaves, self.leavecount)
    
    def traverseM(self):
        return traverseF(self.leaves, [])

def putta(root, value, level, leaves, leavecount):
    # print(leaves)
    new_node = Node(value)
    if root is None:
        new_node.level = level
        root = new_node
        root.parent = root
        if root.value.isnumeric():
            leaves.append(root)
            leavecount += 1
    elif root.value == "[,":
        if root.right != None:
            if root.right.value == "[,]" or root.right.value.isnumeric():
                root.value += value
                root.sum = root.left.sum + root.right.sum
                if root.left.sum != root.right.sum:
                    root.balanced = False
                if not root.left.balanced  or not root.right.balanced:
                    root.balanced = False
                return root, leaves,leavecount
            else:
                level += 1
                if root.right != None:
                    root.right, leaves,leavecount = putta(root.right, value, level, leaves,leavecount)
                else:
                    root.right = new_node
                    root.right.level = level
                    root.right.parent = root
                    if root.right.value.isnumeric():
                        leaves.append(root.right)
                        leavecount += 1
        else:
            level += 1
            if root.right != None:
                root.right, leaves,leavecount = putta(root.right, value, level, leaves,leavecount)
            else:
                root.right = new_node
                root.right.level = level
                root.right.parent = root
                if root.right.value.isnumeric():
                    leaves.append(root.right)
                    leavecount += 1
            
    else:
        if root.left == None:
            new_node.level = level+1
            root.left = new_node
            root.left.parent = root
            if root.left.value.isnumeric():
                leaves.append(root.left)
                leavecount += 1
        else:
            if root.left.value.isnumeric():
                #Add "," to rootval if that isnt done
                if value == "," and root.value == "[":
                    root.value += value
                    # root.sum = int(root.left.value)
                    return root, leaves,leavecount
                
                #Check if root.right is numberic
                elif root.right.value.isnumeric(): #FINNS CHANS ATT DENNA ÄR VÄRDELÖS
                    #Add "]" to rootval if that hasnt been done
                    if value == "]" and root.value == "[,":
                        root.value += value
                        # root.sum += root.right.sum
                        return root, leaves,leavecount
                else:
                    level += 1
                    if root.right != None:
                        root.right, leaves,leavecount = putta(root.right, value, level, leaves,leavecount)
                    else:
                        root.right = new_node
                        root.right.level = level
                        root.right.parent = root
                        if root.right.value.isnumeric():
                            leaves.append(root.right)
                            leavecount += 1
            elif root.left.value == "[,]":
                if value == ",":
                    root.value += value
                    return root, leaves, leavecount
            else:
                level += 1
                if root.left != None:
                    root.left, leaves,leavecount = putta(root.left, value, level, leaves,leavecount)
                else:
                    root.left = new_node
                    root.left.level = level
                    root.left.parent = root
                    if root.left.value.isnumeric():
                        leaves.append(root.left)
                        leavecount += 1
                # root.left = putta(root.left, value, level)
    return root, leaves,leavecount

# Function to  print level order traversal of tree 

def traverseF(leaves, matches):
    
    i = 0
    copy_leaves = leaves
    while len(leaves)<i:
        j = 0
        match_count = 0
        print(copy_leaves[j].value, end = " ")
        print(leaves[i].value)
        while copy_leaves:
            
            if copy_leaves[j] != leaves[i]:
                leveldiff = copy_leaves[j].level - leaves[i].level
                if leveldiff < 0:
                    if 2**abs(leveldiff) == (int(copy_leaves[j].value)/int(leaves[i].value)):
                        match_count += 1
                        # leaves.pop(j)
                        # used_nodes.append(node)
                elif leveldiff >0:
                    if 2**abs(leveldiff) == (int(leaves[i].value)/int(copy_leaves[j].value)):
                        match_count += 1
                        # leaves.pop(j)
                        # used_nodes.append(node)
                else:
                    if copy_leaves[j].value == leaves[i].value:
                        match_count += 1  
                        # leaves.pop(j)
                        # used_nodes.append(node)
            j +=1
        
        leaves[i].matches = match_count
        matches.append(leaves[i])
        i += 1

    # for leave in leaves:
    #     print(leave.value)
    #     match_count = 0
    #     for node in leaves:
    #         if node != leave:
    #             leveldiff = node.level - leave.level
    #             if leveldiff < 0:
    #                 if 2**abs(leveldiff) == (int(node.value)/int(leave.value)):
    #                     match_count += 1
    #                     # used_nodes.append(node)
    #             elif leveldiff >0:
    #                 if 2**abs(leveldiff) == (int(leave.value)/int(node.value)):
    #                     match_count += 1
    #                     # used_nodes.append(node)
    #             else:
    #                 if node.value == leave.value:
    #                     match_count += 1  
    #                     # used_nodes.append(node)
        
    return matches
   
def main():
    
    s = """3
[[3,7],6]
40
[[2,3],[4,5]]

"""

    rows  = s.split("\n")
    j = 0
    for row in rows:

        if j == 0:
            j+= 1
            continue
        if row == "":
            continue
        # print(row)
        b = Tree()
        oneval = False
        try:
            row = int(row)
            oneval = True
        except:
            pass
        #-------------------
   
        if oneval == False:
            val = ""
            i = 0
            while i <len(row):
                if row[i].isnumeric() or row[i] == "*":
                    while row[i].isnumeric()or row[i] == "*":
                        val += row[i]
                        i += 1
                    b.put(val)
                    val = ""
                
                b.put(row[i])
                i += 1
    
            matches = b.traverseM()
            max_matches = 0
            for matchnode in matches:
                if matchnode.matches >= max_matches:
                    max_matches = matchnode.matches

            print(b.leavecount-1-max_matches)
            
        else:
            print(0)
        j += 1
main()