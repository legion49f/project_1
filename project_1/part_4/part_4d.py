# this is the iterative version of a AVL Tree

class Node(object): # Move delete methods to AVL_Tree Class after professor leaves comment to refactor this because it no londer makes
    # sense to have this here since you also moved the insert method to the tree class
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.height = 0

    def search(self, value):
        current = None
        nodes = [self]
        while nodes:
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


class AVL_Tree(object):
    def __init__(self):
        self.root = None
        self.output = []

    def delete(self, value):
        if self.root is not None:
            self.root.delete(value)
            current = self.root

            non_leaf_nodes, parent = self.find_parent_nodes(current, value)
            self.insert_child_node(parent, value)

            self.update_heights_of_parent_nodes(non_leaf_nodes)
            self.rebalance_tree(non_leaf_nodes)
        return False

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return
        current = self.root

        non_leaf_nodes, parent = self.find_parent_nodes(current, value)
        self.insert_child_node(parent, value)

        self.update_heights_of_parent_nodes(non_leaf_nodes)
        self.rebalance_tree(non_leaf_nodes)

    def insert_child_node(self, parent, value):
        if value < parent.value:
            parent.leftNode = Node(value)
        elif value > parent.value:
            parent.rightNode = Node(value)

    def find_parent_nodes(self, node, value):
        parent = None
        non_leaf_nodes = []
        while node:
            non_leaf_nodes = [node] + non_leaf_nodes
            parent = node

            if value < node.value:
                node = node.leftNode
            else:
                node = node.rightNode

        return non_leaf_nodes, parent

    def rebalance_tree(self, parents):
        for i, parent in enumerate(parents):
            if i + 1 < len(parents):
                self.rebalance_subtree(parent, parents[i + 1])
            else:
                self.rebalance_subtree(parent, None)

    def update_heights_of_parent_nodes(self, parents):
        for node in parents:
            self.set_height(node)

    def calculate_balance_factor(self, node):
        if not self.root:
            return 0
        if not node: # remove after testing
            node = self.root
        return self.get_height(node.leftNode) - self.get_height(node.rightNode)

    def rotate_left(self, prev_root, temp_root):
        new_root = prev_root.rightNode
        child_nodes = new_root.leftNode

        prev_root.rightNode = child_nodes
        new_root.leftNode = prev_root

        if temp_root:
            if new_root.value < temp_root.value:
                temp_root.leftNode = new_root
            else:
                temp_root.rightNode = new_root
        else:
            self.root = new_root

        self.set_height(prev_root)
        self.set_height(new_root)

        return new_root

    def rotate_right(self, prev_root, temp_root):
        root = prev_root.leftNode
        child_nodes = root.rightNode
        prev_root.leftNode = child_nodes
        root.rightNode = prev_root

        if temp_root is not None:
            if root.value < temp_root.value:
                temp_root.leftNode = root
            else:
                temp_root.rightNode = root
        else:
            self.root = root

        self.set_height(prev_root)
        self.set_height(root)
        return root

    def rebalance_subtree(self, node, parent):
        bc = self.calculate_balance_factor(node)
        if bc > 1:
            return self.rotate_left_subtree(node, parent)
        if bc < -1:
            return self.rotate_right_subtree(node, parent)
        return node

    def rotate_right_subtree(self, node, parent):
        if self.calculate_balance_factor(node.rightNode) > 0:
            node.rightNode = self.rotate_right(node.rightNode, node)
        return self.rotate_left(node, parent)

    def rotate_left_subtree(self, node, parent):
        if self.calculate_balance_factor(node.leftNode) < 0:
            node.leftNode = self.rotate_left(node.leftNode, node)
        return self.rotate_right(node, parent)

    def set_height(self, node):
        node.height = max(self.get_height(node.leftNode), self.get_height(node.rightNode)) + 1

    def get_height(self, node):
        if node is not None:
            return node.height
        return -1

    def traversal(self, traversal_type, start):  # not needed for question but still nice to have for debugging 
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

    def pre_order(self, start):  # not needed for question but still nice to have
        if start is not None:
            self.output.append(start.value)
            self.pre_order(start.leftNode)
            self.pre_order(start.rightNode)
        return self.output

    def post_order(self, start):  # not needed for question but still nice to have
        if start is not None:
            self.post_order(start.leftNode)
            self.post_order(start.rightNode)
            self.output.append(start.value)
        return self.output

    def in_order(self, start):  # used iterative method because could not figure the better method
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

    def find_min_value_iterative(self, start):  # Done
        while (start.leftNode is not None):
            start = start.leftNode
        return start.value

    def find_max_value_iterative(self, start):  # Done
        while (start.rightNode is not None):
            start = start.rightNode
        return start.value

    def match_node(self, start, value):  # unused might remove later
        ###Returns the Node with the Value ###
        while start is not None:  # Find the node we are looking for if it exists
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

# for item in list1:
#     tree1.insert(item)

# for item in list2:
#     tree2.insert(item)

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

tree1 = AVL_Tree()
list1 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

tree2 = AVL_Tree()
list2 = [ 100, 53, 172, 24, 64, 150, 200, 12, 33, 60, 98, 130] #

tree3 = AVL_Tree()
list3 = [5, 3, 9, 2, 4, 1, 10]

tree4 = AVL_Tree()
list4 = [3, 11, 12, 5, 9, 2, 4, 1, 10]


for item in list1:
    tree1.insert(item)
    # print('Test 1 - Balance Factor is: ', tree1.calculate_balance_factor(tree1.root))

for item in list2:
    tree2.insert(item)
    # print('Test 2 - Balance Factor is: ', tree2.calculate_balance_factor(tree2.root))

for item in list3:
    tree3.insert(item)
    # print('Test 3 - Balance Factor is: ', tree3.calculate_balance_factor(tree3.root))

for item in list4:
    tree4.insert(item)
    # print('Test 4 - Balance Factor is: ', tree4.calculate_balance_factor(tree4.root))

# Deletion Test

for item in list1:
    tree1.delete(item)
    print('Test 1 - Balance Factor is: ', tree1.calculate_balance_factor(tree1.root))

for item in list2:
    tree2.delete(item)
    print('Test 2 - Balance Factor is: ', tree2.calculate_balance_factor(tree2.root))

for item in list3:
    tree3.delete(item)
    print('Test 3 - Balance Factor is: ', tree3.calculate_balance_factor(tree3.root))

for item in list4:
    tree4.delete(item)
    print('Test 4 - Balance Factor is: ', tree4.calculate_balance_factor(tree4.root))