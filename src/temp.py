class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.left = None
        self.right = None

class Wavl:
    def __init__(self) -> None:
        self.root = Node()
    # Inorder traversal
    def inorder(self):
        if self.root is not None:
            # Traverse left
            self.inorder(self.root.left)

            # Traverse root
            print(str(self.root.value) + "->", end=' ')

            # Traverse right
            self.inorder(self.root.right)


    # Insert a node
    def insert(self, node, key):

        # Return a new node if the tree is empty
        if node is None:
            return Node(key)

        # Traverse to the right place and insert the node
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        return node


    # Find the inorder successor
    def minValueNode(self, node):
        current = node

        # Find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current


    # Deleting a node
    def deleteNode(self, key):

        # Return if the tree is empty
        if self.root is None:
            return self.root

        # Find the node to be deleted
        if key < self.root.key:
            self.root.left = self.deleteNode(self.root.left, key)
        elif(key > self.root.key):
            self.root.right = self.deleteNode(self.root.right, key)
        else:
            # If the node is with only one child or no child
            if self.root.left is None:
                temp = self.root.right
                self.root = None
                return temp

            elif self.root.right is None:
                temp = self.root.left
                self.root = None
                return temp

            # If the node has two children,
            # place the inorder successor in position of the node to be deleted
            temp = self.minValueNode(self.root.right)

            self.root.key = temp.key

            # Delete the inorder successor
            self.root.right = self.deleteNode(self.root.right, temp.key)

        return self.root
