def createStack():
    stack = []
    return stack


def push(stack, item):
    stack.append(item)
    print(item, "pushed in to stack")


def pop(stack):
    if len(stack) == 0:
        print("stack is empty")
    else:
        return stack.pop()


def peek(stack):
    if len(stack) == 0:
        print("stack is empty")
    else:
        return stack[len(stack) - 1]


stack = createStack()
push(stack, 2)
push(stack, 6)
push(stack, 4)
push(stack, 5)
print(pop(stack), "poped from stack")
