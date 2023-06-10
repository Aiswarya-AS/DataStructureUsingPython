class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newnode = StackNode(data)
        if self.top is None:
            self.top = newnode

        else:
            last = self.top
            while last.next:
                last = last.next
            last.next = newnode

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next

    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            prev = self.top
            temp = self.top.next
            while temp.next:
                prev = prev.next
                temp = temp.next
            prev.next = None

    def peek(self):
        if self.top is None:
            print("stack is empty")
        else:
            print(self.top.data)


stack = Stack()
stack.push(10)
stack.push(100)
stack.push(78)
stack.push(56)
stack.push(89)
stack.push(19)
stack.push(45)
stack.display()
stack.pop()
print("")
stack.display()
print()
stack.peek()
