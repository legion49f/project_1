from random import randint

class Node2(object):
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
        self.parent = None

    def insert(self, value): # Done ### Setting the Parent Node is not passing the TEST, Fix later...
        """Helper Function for Adding because it can be reused later"""
        node = Node2(value)
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
class Tree(object):
    def __init__(self):
        self.root = None
        self.output = []
    
    def insert(self, value):
        if self.root is not None:
            return self.root.insert(value) # this is not a recursive call it just calls the method of the Node Class
        else:
            self.root = Node2(value)
            # take this out later
            return True

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


def getRandomArray(n) -> list:
    """Return an array of N integers with a range one order of magnite larger from the input."""
    arr = []
    power = 0
    _ = n
    while( _ > 0):
        _ = _ // 10
        power+=1
    rand_int_range = 10**power

    while len(arr) != n:
        rand_int = randint(0, rand_int_range)
        if rand_int not in arr:
            arr.append( rand_int )
    
    return arr

arr = getRandomArray(10000)

BST = Tree()

AVL = AVL_Tree()

for item in arr:
    BST.insert(item)
    AVL.insert(item)


