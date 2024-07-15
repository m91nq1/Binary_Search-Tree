class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

       def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

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

    
    def depth_first_search(self):  
        return self.traverse()

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    def find_min(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current.value

    
    def find_max(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current.value

   
    def traverse(self):
        sorted_list = []
        self._traverse(self.root, sorted_list)
        return sorted_list

    def _traverse(self, node, sorted_list):
        if node is not None:
            self._traverse(node.left, sorted_list)
            sorted_list.append(node.value)
            self._traverse(node.right, sorted_list)


bst = BinarySearchTree()


weights = [20, 12, 7, 22, 15, 26, 18, 120]


for weight in weights:
    bst.insert(weight)


sorted_weights = bst.depth_first_search()
print("Sorted list of biltong weights:", sorted_weights)

minimum_weight = bst.find_min(bst.root)
maximum_weight = bst.find_max(bst.root)

print("Minimum value:", minimum_weight)
print("Maximum value:", maximum_weight)

ratio = maximum_weight / minimum_weight
print("Ratio of maximum to minimum weight:", ratio)





