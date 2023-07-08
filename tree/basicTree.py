class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def delete_child(self, value):
        for i, child in enumerate(self.children):
            if child.value == value:
                del self.children[i]
                return
            else:
                self.delete_child(value)

    def display(self, level=0):
        print("" * level + self.value)
        for i in self.children:
            i.display(level + 1)

    # display node if they have more than 2 children
    def display_child(self, level=0):
        if len(self.children) > 2:
            print(" " * level + self.value)
        for child in self.children:
            child.display_child(level + 1)

    def dfs(self):
        print(self.value)
        for child in self.children:
            child.dfs()

    def bfs(self):
        queue = [self]

        while queue:
            node = queue.pop(0)
            print(node.value)
            queue.extend(node.children)


root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)

root.delete_child("B")
root.display()
