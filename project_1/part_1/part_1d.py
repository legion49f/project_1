# this is the iterative version of a tree

class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.parent = None

    def insert(self, value): # Done ### Setting the Parent Node is not passing the TEST, Fix later...
        """Helper Function for Adding because it can be reused later"""
        node = Node(value)
        current = self
        parent = None
        while True:
            parent = current
            if node.value < parent.value:
                current = current.leftNode
                if current is None:
                    parent.leftNode = node
                    return
            elif node.value > parent.value:
                current = current.rightNode
                if current is None:
                    parent.rightNode = node
                    return

    def search(self, value):
        current = None
        nodes = [self]
        while len(nodes):
            temp = nodes.pop(0)
            if temp.value == value:
                current = temp
            if self.has_left_child(temp):
                nodes.append(temp.leftNode)
            if self.has_right_child(temp):
                nodes.append(temp.rightNode)
        return current, temp

    def delete(self, value):
        if self is None:
            return None

        self.delete_root(value)
        current, head = self.search(value)
        if current is not None:
            head_value = head.value
            self.delete_leaf_node(head)
            current.value = head_value
            
    def delete_root(self, value):
        if self.has_right_child(self) is False and self.has_left_child(self) is False:
            if self.value == value:
                self.value = None

    def delete_leaf_node(self, node):
        nodes = [self]
        while len(nodes) > 0:
            current = nodes.pop(0)
            if current is node:
                return
            if self.has_right_child(current):
                if current.rightNode is node:
                    current.rightNode = None
                    return
                nodes.append(current.rightNode)
            if self.has_left_child(current):
                if current.leftNode is node:
                    current.leftNode = None
                    return
                nodes.append(current.leftNode)

    def has_left_child(self, node):
        return node.leftNode is not None

    def has_right_child(self, node):
        return node.rightNode is not None

class Tree(object):
    def __init__(self):
        self.root = None
        self.output = []
    
    def insert(self, value):
        if self.root is not None:
            return self.root.insert(value) # this is not a recursive call it just calls the method of the Node Class
        else:
            self.root = Node(value)
            # take this out later
            return True

    def delete(self, value):
        if self.root is not None:
            return self.root.delete(value)
        return False

    def traversal(self, traversal_type, start): # not needed for question but still nice to have
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

    def pre_order(self, start): # not needed for question but still nice to have
        if start is not None:
            self.output.append(start.value)
            self.pre_order(start.leftNode)
            self.pre_order(start.rightNode)
        return self.output

    def post_order(self, start): # not needed for question but still nice to have
        if start is not None:
            self.post_order(start.leftNode)
            self.post_order(start.rightNode)
            self.output.append(start.value)
        return self.output

    def in_order(self, start): # used iterative method because could not figure out a better method
        lst = []
        while True:
            if start is not None:
                lst.append(start)
                start = start.leftNode
            elif lst:
                start = lst.pop()
                self.output.append(start.value)
                start = start.rightNode
            else:
                break
        return self.output

    def find_min_value_iterative(self, start): # Done
        while(start.leftNode is not None):
            start = start.leftNode
        return start.value

    def find_max_value_iterative(self, start): # Done
        while(start.rightNode is not None):
            start = start.rightNode
        return start.value
        
    def match_node(self, start, value): # unused might remove later
        ###Returns the Node with the Value ###
        while start is not None: # Find the node we are looking for if it exists
            if value > start.value:
                start = start.rightNode
            elif value < start.value:
                start = start.leftNode
            else:
                return start
        return None

    def find_next_iterative(self, start, value):
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

    def find_previous_iterative(self, start, value):
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

# tree1 = Tree()
# list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

# tree2 = Tree()
# list2 = [ 100, 53, 172, 24, 64, 150, 200, 12, 33, 60, 98, 130] # 

# tree3 = Tree()
# list3 = [5, 3, 9, 2, 4, 1, 10]

# # for item in list1:
# #     tree1.insert(item)

# # for item in list2:
# #     tree2.insert(item)

# for item in list3:
#     tree3.insert(item)


# print( Tree.traversal(tree1, traversal_type='pre_order', start=tree1.root ) )
# print( Tree.traversal(tree2, traversal_type='post_order', start=tree2.root ) )
# print( Tree.traversal(tree3, traversal_type='in_order', start=tree3.root) ) 

# print( Tree.traversal(tree2, traversal_type='post_order', start=tree2.root ) )
# print( Tree.traversal(tree2, traversal_type='pre_order', start=tree2.root ) )
# print( Tree.traversal(tree2, traversal_type='in_order', start=tree2.root ) )

# print( tree1.find_min_value_iterative(tree1.root) )
# print( tree2.find_min_value_iterative(tree2.root) )
# print( tree3.find_min_value_iterative(tree3.root) )

# print( tree1.find_max_value_iterative(tree1.root) )
# print( tree2.find_max_value_iterative(tree2.root) )
# print( tree3.find_max_value_iterative(tree3.root) )

# print( tree1.match_node(tree1.root, 0) )
# print( tree2.match_node(tree2.root, 180) )
# print( tree3.match_node(tree3.root, 9) )

# print( Tree.traversal(tree1, traversal_type='in_order', start=tree1.root ) )
# print( Tree.traversal(tree2, traversal_type='in_order', start=tree2.root ) )
# print( Tree.traversal(tree3, traversal_type='in_order', start=tree3.root ) )

# print( tree1.find_next_iterative(tree1.root, 7) )
# print( tree2.find_next_iterative(tree2.root, 150) )
# print( tree3.find_next_iterative(tree3.root, 4) )

# print( tree1.find_previous_iterative(tree1.root, 0) )
# print( tree2.find_previous_iterative(tree2.root, 172) )
# print( tree3.find_previous_iterative(tree3.root, 4) )

# print( tree1.delete(10) )
# print( tree2.delete(24) )
# print( tree3.delete(4) )

# for item in list1:
#     tree1.delete(item)

# for item in list2:
#     tree2.delete(item)

# for item in list3:
#     tree3.delete(item)

# print( Tree.traversal(tree1, traversal_type='in_order', start=tree1.root ) )
# print( Tree.traversal(tree2, traversal_type='in_order', start=tree2.root ) )
# print( Tree.traversal(tree3, traversal_type='in_order', start=tree3.root) ) 


# list3 = [5, 3, 9, 2, 4, 1, 10]

# tree4 = Tree()
# for item in list3:
#     tree4.insert(item)
    # print( Tree.traversal(tree4, traversal_type='in_order', start=tree4.root) ) 

# for item in list3:
#     # print( Tree.traversal(tree4, traversal_type='in_order', start=tree4.root) ) 
#     tree4.delete(item)
#     print( Tree.traversal(tree4, traversal_type='in_order', start=tree4.root) ) 


# print( Tree.traversal(tree4, traversal_type='in_order', start=tree4.root) ) 


# print(tree4.match_node(tree4.root, 5))
# print(tree4.match_node(tree4.root, 9))