class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    def Enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return
        else:
            self.rear.next = new_node
            self.rear = new_node

    def Deqeue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        temp.next = None
        if self.front is None:
            self.rear = None

    def queueDisplay(self):
        temp = self.front
        while temp.next:
            print(temp.data, "-->", end=" ")
            temp = temp.next


queue = Queue()
queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(40)
queue.Enqueue(50)
queue.queueDisplay()
queue.Deqeue()
print("\n")
queue.queueDisplay()
