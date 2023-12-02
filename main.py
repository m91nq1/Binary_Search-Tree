# Define a Node class to represent each element in the binary search tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Define a BinarySearchTree class to represent the binary search tree data structure
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a value into the binary search tree
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    # Helper function for inserting a value recursively
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # Perform depth-first search to get a sorted list of values
    def depth_first_search(self):  # Corrected method name
        return self.traverse()

    # Search for a value in the binary search tree
    def search(self, value):
        return self._search(self.root, value)

    # Helper function for searching a value recursively
    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    # Find the minimum value in the binary search tree
    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.value

    # Find the maximum value in the binary search tree
    def find_max(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.value

    # Traverse the binary search tree in-order and return a sorted list of values
    def traverse(self):
        sorted_list = []
        self._traverse(self.root, sorted_list)
        return sorted_list

    # Helper function for in-order traversal
    def _traverse(self, node, sorted_list):
        if node is not None:
            self._traverse(node.left, sorted_list)
            sorted_list.append(node.value)
            self._traverse(node.right, sorted_list)

# Create a BinarySearchTree instance
bst = BinarySearchTree()

# List of weights
weights = [20, 12, 7, 22, 15, 26, 18, 120]

# Insert weights into the binary search tree
for weight in weights:
    bst.insert(weight)

# Perform depth-first search to get sorted weights
sorted_weights = bst.depth_first_search()
print("Sorted list of biltong weights:", sorted_weights)

# Find minimum and maximum weights
minimum_weight = bst.find_min(bst.root)
maximum_weight = bst.find_max(bst.root)

print("Minimum value:", minimum_weight)
print("Maximum value:", maximum_weight)

# Calculate the ratio of maximum to minimum weight
ratio = maximum_weight / minimum_weight
print("Ratio of maximum to minimum weight:", ratio)





