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

    def delete(self, data):
        """ Deletes a data point from the tree"""
        # Node is a leaf Node to be deleted
        if self is None:
            return False # tree is empty
        
        if self.value > data:
            # check for leftNode
            if self.leftNode is not None:
                self = self.leftNode
                self.delete(data)
            else:
                return False # the item doesnt exist

        elif self.value < data:
            if self.rightNode is not None:
                self = self.rightNode
                self.delete(data)
            else:
                return False # item doesnt exist

        else: #delete data
            # check for leftNode only, rightNode only, both Nodes or no Nodes
            if self.leftNode is None and self.rightNode is None:
                self = None
                # print('No children')
            elif self.leftNode is not None and self.rightNode is None:
                # it has only a leftNode
                self.parent.leftNode = self.leftNode
                
            elif self.rightNode is None and self.rightNode is not None:
                # it has only a rightNode
                self.parent.rightNode = self.leftNode
                
            else:
                # it has both left and right Nodes
                pass
                # print('Both Children')
            

class AVL_Tree(object): # Recursive
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

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)
        return False

    def traversal(self, traversal_type, start):
        """Traverses the tree, needs Type of travesal and Start Node"""
        self.output = []
        if traversal_type == 'pre_order':
            self.output = self.pre_order(start)
            return self.output
        elif traversal_type == 'post_order':
            self.output = self.post_order(start)
            return self.output
        elif traversal_type == 'in_order':
            self.output = self.in_order(start)
            return self.output
        else:
            return []

    def pre_order(self, start):
        if start is not None:
            self.output.append(start.value)
            self.pre_order(start.leftNode)
            self.pre_order(start.rightNode)
        return self.output

    def post_order(self, start):
        if start is not None:
            self.post_order(start.leftNode)
            self.post_order(start.rightNode)
            self.output.append(start.value)
        return self.output

    def in_order(self, start):
        if start is not None:
            self.in_order(start.leftNode)
            self.output.append(start.value)
            self.in_order(start.rightNode)
        return self.output

    def find_min_value_recursive(self, start):
        if start is None:
            return False
        while start.leftNode is not None:
            start = start.leftNode
            self.find_min_value_recursive(start)
        return start.value

    def find_max_value_recursive(self, start):
        if start is None:
            return False
        while start.rightNode is not None:
            start = start.rightNode
            self.find_max_value_recursive(start)
        return start.value
        
    def find_next_recursive(self, start, value):
        # not working and running out of time going the easy route
        # if start.value == value:
        #     if start.rightNode is not None:
        #         start = start.rightNode
        #         while(start.leftNode):
        #             start = start.leftNode
        #         return start.value
        #     if start.parent is None:
        #         return False
        #     while start.parent is not None:
        #         if start.parent.leftNode == start:
        #             return start.parent
        #         start = start.parent
        #     return False

        # elif start.value < value:
        #     start = start.leftNode
        #     self.find_next_recursive(start, value)
        
        # else:
        #     start = start.rightNode
        #     self.find_next_recursive(start, value)
        # easy route 
        self.in_order(start)
        index = 0
        if value not in self.output:
            return False
        elif value == self.output[-1]:
            return False
        for item in self.output:
            index += 1
            if item == value:
                break
        return self.output[index]

    def find_previous_recursive(self, start, value):
        self.in_order(start)
        index = 0
        if value not in self.output:
            return False
        elif value == self.output[0]:
            return False
        for item in self.output:
            if item == value:
                break
            index += 1
        index -= 1
        return self.output[index]

tree1 = AVL_Tree()
list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

tree2 = AVL_Tree()
list2 = [ 100, 53, 172, 24, 64, 150 ] # , 200, 12, 33, 60, 98, 130

tree3 = AVL_Tree()
list3 = [5, 3, 9, 2, 4, 1, 10]

for item in list1:
    tree1.insert(item)

for item in list2:
    tree2.insert(item)

for item in list3:
    tree3.insert(item)


# print( Tree.traversal(tree1, traversal_type='pre_order', start=tree1.root ) )
# print( Tree.traversal(tree2, traversal_type='post_order', start=tree2.root ) )
# print( Tree.traversal(tree3, traversal_type='in_order', start=tree3.root) ) 

# print( Tree.traversal(tree2, traversal_type='post_order', start=tree2.root ) )
# print( Tree.traversal(tree2, traversal_type='pre_order', start=tree2.root ) )
# print( Tree.traversal(tree2, traversal_type='in_order', start=tree2.root ) )

print( tree1.find_min_value_recursive(tree1.root) )
print( tree2.find_min_value_recursive(tree2.root) )
print( tree3.find_min_value_recursive(tree3.root) )

print( tree1.find_max_value_recursive(tree1.root) )
print( tree2.find_max_value_recursive(tree2.root) )
print( tree3.find_max_value_recursive(tree3.root) )

# print( tree1.find_next_recursive(tree1.root, 11) )
# print( tree2.find_next_recursive(tree2.root, 172) )
# print( tree3.find_next_recursive(tree3.root, 4) )

# print( tree1.find_previous_recursive(tree1.root, 0) )
# print( tree2.find_previous_recursive(tree2.root, 172) )
# print( tree3.find_previous_recursive(tree3.root, 4) )

# print( tree1.delete(10) )
# print( tree2.delete(24) )
# print( tree3.delete(4) )

# print( Tree.traversal(tree1, traversal_type='in_order', start=tree1.root ) )
# print( Tree.traversal(tree2, traversal_type='in_order', start=tree2.root ) )
# print( Tree.traversal(tree3, traversal_type='in_order', start=tree3.root) ) 