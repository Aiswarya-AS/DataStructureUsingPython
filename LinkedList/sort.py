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

    def sort(self):
        current = self.head
        index = None
        if self.head is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next


linkedList = SinglyLinkedList()
linkedList.insertion_at_begining(36)
linkedList.insertion_at_begining(16)
linkedList.insertion_at_begining(45)
linkedList.insertion_at_begining(100)
linkedList.insertion_at_begining(10)
linkedList.insertion_at_begining(8)
linkedList.display()
linkedList.sort()
print()
print("After sorting...")
linkedList.display()
