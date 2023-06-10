class Queue:
    def __init__(self, c):
        self.queue = []
        self.rear = self.fornt = 0
        self.capacity = c

    def Enqueue(self, data):
        if self.capacity == self.rear:
            print("Queue is full")
        else:
            self.queue.append(data)
            self.rear += 1

    def Dequeue(self):
        if self.fornt == self.rear:
            print("queue is empty")
        else:
            self.queue.pop(0)
            self.rear -= 1

    def display(self):
        for i in self.queue:
            print(i, "<--", end="")


queue = Queue(30)
queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(400)
queue.Enqueue(50)
queue.Enqueue(60)
queue.Enqueue(70)
queue.display()
queue.Dequeue()
print()
queue.display()
