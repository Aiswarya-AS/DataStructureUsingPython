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
