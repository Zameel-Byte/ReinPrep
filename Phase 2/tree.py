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

    def leveler(root):
        q = []
        q.append(root)
        while len(q) != 0:
            ele = q.pop(0)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            print(ele.data)

    def search_ele(self, root, value):
        if root.data == value or root is None:
            return root
        if value < root.data and root.left is not None:
            return self.search_ele(root.left, value)
        if value > root.data and root.right is not None:
            return self.search_ele(root.right, value)

    def sum_subtree(self, root):
        sum = root.data
        if root.left is not None:
            sum += self.sum_subtree(root.left)
        if root.right is not None:
            sum += self.sum_subtree(root.right)
        return sum

    def height(self, root):
        if root is None:
            return -1
        left_height = self.height(root.left)
        right_height = self.height(root.right)

        return 1 + max(left_height, right_height)

