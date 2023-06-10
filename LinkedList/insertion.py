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

    def insertion_at_end(self, data):
        newnode = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = newnode

    # insertion at given position
    def insertion_at_position(self, data, pos):
        new_node = Node(data)
        prev = self.head
        for i in range(1, pos - 1):
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node

        # insertion after a given node

    def insertion_after(self, data, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                break
            else:
                temp = temp.next
        if temp is not None:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        else:
            print("Node is not present in the list")

    # insert before a given node
    def insertion_before(self, data, x):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            if temp.next.data == x:
                break
            else:
                temp = temp.next
        if temp.next is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node

    def printMiddle(self):
        temp = self.head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        midIndex = length // 2
        temp = self.head
        while midIndex != 0:
            temp = temp.next
            midIndex -= 1
        print(temp.data)

    def print_alternate(self):
        temp = self.head
        while temp:
            print(temp.data, "->", end=" ")
            temp = temp.next.next


linkedList = SinglyLinkedList()
linkedList.insertion_at_begining(50)
linkedList.insertion_at_begining(60)
linkedList.insertion_at_begining(70)
linkedList.insertion_at_begining(80)
linkedList.insertion_at_begining(90)
linkedList.insertion_at_begining(100)
linkedList.insertion_at_end(1000)
linkedList.display()
