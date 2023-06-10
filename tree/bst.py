class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def insert(node, key):
    if node is None:
        return Node(key)
    if node.data > key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def inorder(node):
    if node.left:
        inorder(node.left)
    print(node)
    if node.right:
        inorder(node.right)


def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node)


def preorder(node):
    print(node)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)


def min_value(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def deletion(root, data):
    if root is None:
        return root
    if root.data > data:
        root.left = deletion(root.left, data)
    elif root.data < data:
        root.right = deletion(root.right, data)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_value(temp.right)
        root.data = temp.data
        root.right = deletion(root.right, temp.data)
    return root


def search(root, x):
    if root.data == x:
        print("Node found")
        return
    elif root.data > x:
        if root.left:
            search(root.left, x)
        else:
            print("Not found")
    else:
        if root.right:
            search(root.right, x)
        else:
            print("Node not found")


def second_largest(root):
    c = [0]
    secondLargestUntill(root, c)


def secondLargestUntill(root, c):
    if root is None or c[0] > 2:
        return
    secondLargestUntill(root.right, c)
    c[0] += 1
    if c[0] == 2:
        print("Seconf largest", root.data)
    secondLargestUntill(root.left, c)
