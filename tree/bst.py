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


# check is bst or not
previous = None


def isBST(root):
    global previous
    previous = None
    return isBST_inorder(root)


def isBST_inorder(root):
    global previous
    if root is None:
        return True
    if isBST_inorder(root.left) is False:
        return False
    if previous is not None and previous.data > root.data:
        return False
    previous = root
    return isBST_inorder(root.right)


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
inorder(root)
print("level order")
# level_order(root)
# second_largest(root)
search(root, 35)
deletion(root, 70)
print("after deletion")
# level_order(root)

# check for BST
# if(isBST(root)):
#     print("Binary Tree is BST")
# else:
#     print("Binary Tree is not Bst")
