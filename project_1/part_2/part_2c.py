# this is the sort algo.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.parent = None # parent node is needed to implement delete, find next and find previous

    def insert(self, data):
        """Helper Function for Adding because it can be reused later"""
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftNode:
                return self.leftNode.insert(data)
            else:
                self.leftNode = Node(data)
                self.leftNode.parent = self
                return True

        else:
            if self.rightNode:
                return self.rightNode.insert(data)
            else:
                self.rightNode = Node(data)
                self.rightNode.parent = self
                return True            

class Tree(object):
    def __init__(self):
        self.root = None
        self.output = []
    
    def insert(self, data):
        if self.root is not None:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            # take this out later
            return True

    def traversal(self, traversal_type, start):
        """Traverses the tree, needs Type of travesal and Start Node"""
        self.output = []
        if traversal_type == 'in_order':
            self.output = self.in_order(start)
            return self.output
        else:
            return []

    def in_order(self, start):
        if start is not None:
            self.in_order(start.leftNode)
            self.output.append(start.value)
            self.in_order(start.rightNode)
        return self.output



tree1 = Tree()
list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

tree2 = Tree()
list2 = [ 100, 53, 172, 24, 64, 150 ] # , 200, 12, 33, 60, 98, 130

tree3 = Tree()
list3 = [5, 3, 9, 2, 4, 1, 10]

for item in list1:
    tree1.insert(item)

for item in list2:
    tree2.insert(item)

for item in list3:
    tree3.insert(item)


print( Tree.traversal(tree1, traversal_type='in_order', start=tree1.root ) )
print( Tree.traversal(tree2, traversal_type='in_order', start=tree2.root ) )
print( Tree.traversal(tree3, traversal_type='in_order', start=tree3.root) ) 
