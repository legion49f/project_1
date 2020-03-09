class Node(object):
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

class Tree(object):
    def __init__(self):
        self.root = None
        self.output = []
    
    def insert(self, data):
        """ insert into the tree unless the value repeats """
        if self.root is None:
           self.root = Node(data)
        else:
            if self.root.value == data:
                return False

            elif self.root.value > data:
                if self.root.leftNode:
                    return self.leftNode.insert(data)
                else:
                    self.leftNode = Node(data)
                    return True

            else:
                if self.root.rightNode:
                    return self.rightNode.insert(data)
                else:
                    self.rightNode = Node(data)
                    return True


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
            return 'traversal type not supported'

    def pre_order(self, start):
        if start is not None:
            # print(start.value)
            self.output.append(start.value)
            if start is not None:
                self.pre_order(start.leftNode)
            if start is not None:
                self.pre_order(start.rightNode)
        return self.output

    def post_order(self, start):
        if start is not None:
            if start is not None:
                self.post_order(start.leftNode)
            if start is not None:
                self.post_order(start.rightNode)
            self.output.append(start.value)
        return self.output

    def in_order(self, start):
        if start is not None:
            if start is not None:
                self.in_order(start.leftNode)
            self.output.append(start.value)
            if start is not None:
                self.in_order(start.rightNode)
        return self.output

    def delete_Node(self, value):
        pass

    def find_next_recursive(self, value):
        pass

    def find_previous_recursive(self, value):
        pass

    def find_min_value_recursive(self, value):
        pass

    def find_max_value_recursive(self, value):
        pass

tree1 = Tree()
list1 = [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]

tree2 = Tree()
list2 = [ 100, 53, 172, 24, 64, 150 ] # , 200, 12, 33, 60, 98, 130 

tree3 = Tree()
list3 = [5, 3, 9, 2, 4, 1, 10]

for item in list1:
    tree1.insert(item)

# for item in list2:
#     tree2.insert(item)

# for item in list3:
#     tree3.insert(item)


print( Tree.traversal(tree1, traversal_type='pre_order', start=tree1.root ) )
# print( Tree.traversal(tree2, traversal_type='post_order', start=tree2.root ) )
# print( Tree.traversal(tree3, traversal_type='in_order', start=tree3.root) ) 

# print( Tree.traversal(tree2, traversal_type='post_order', start=tree2.root ) )
# print( Tree.traversal(tree2, traversal_type='pre_order', start=tree2.root ) )
# print( Tree.traversal(tree2, traversal_type='in_order', start=tree2.root ) )