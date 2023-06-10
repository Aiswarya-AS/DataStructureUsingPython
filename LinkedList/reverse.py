class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, "-->", end="")
            temp = temp.next

    def insertion_at_begining(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode

        else:
            newnode.next = self.head
            self.head = newnode

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


linkedList = SinglyLinkedList()
linkedList.insertion_at_begining(36)
linkedList.insertion_at_begining(16)
linkedList.insertion_at_begining(45)
linkedList.insertion_at_begining(100)
linkedList.insertion_at_begining(10)
linkedList.insertion_at_begining(8)
linkedList.display()
