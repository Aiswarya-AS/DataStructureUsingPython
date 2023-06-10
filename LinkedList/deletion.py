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

    def insertion(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def deletion_at_begining(self):
        self.head = self.head.next

    def deletion_at_end(self):
        prev = self.head
        last = self.head.next
        while last.next:
            last = last.next
            prev = prev.next
        prev.next = None

    def deleteion_given_posistion(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(1, pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None


linkedList = SinglyLinkedList()
linkedList.insertion(10)
linkedList.insertion(20)
linkedList.insertion(30)
linkedList.insertion(40)
linkedList.insertion(50)
linkedList.insertion(60)
print("insertion...")
linkedList.display()
linkedList.deletion_at_begining()
print("After deletion...")
linkedList.deletion_at_end()
linkedList.display()
