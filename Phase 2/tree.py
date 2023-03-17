from queue import Queue

Q = Queue()

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def add_element(self, root, value):
        new_node = Node(value)
        if new_node.data < root.data:
            if root.left is not None:
                self.add_element(root.left, value)
            else:
                root.left = new_node
        else:
            if root.right is not None:
                self.add_element(root.right, value)
            else:
                root.right = new_node

    def inorder(self, root):
        if root.left is not None:
            self.inorder(root.left)
        print(root.data, end=" ")
        if root.right is not None:
            self.inorder(root.right)

    def preorder(self, root):
        print(root.data, end=" ")
        if root.left is not None:
            self.preorder(root.left)
        if root.right is not None:
            self.preorder(root.right)

    def postorder(self, root):
        if root.left is not None:
            self.postorder(root.left)
        if root.right is not None:
            self.postorder(root.right)
        print(root.data, end=" ")

    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            ele = q.pop(0)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            print(ele.data)


obj = BST()
root = Node(10)
obj.add_element(root, 7)
obj.add_element(root, 40)
obj.add_element(root, 5)
obj.add_element(root, 9)
obj.add_element(root, 15)
obj.add_element(root, 60)
# obj.inorder(root)
# obj.preorder(root)
# obj.postorder(root)
obj.levelorder(root)

