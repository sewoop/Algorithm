import sys

n = int(sys.stdin.readline())


class Stack:
    def __init__(self):
        self.container = []
        self.size = 0

    def push(self, data):
        self.container.append(data)
        self.size += 1

    def pop(self):
        try:
            res = self.container.pop()
            self.size -= 1
        except:
            res = -1
        print(res)
        return res

    def stackSize(self):
        print(self.size)
        return self.size

    def stackTop(self):
        if self.size == 0:
            print(-1)
        else:
            print(self.container[-1])

    def isEmpty(self):
        if self.size == 0:
            print(1)
            return 1
        else:
            print(0)
            return 0

    def stackPrint(self):
        print(self.container)


stack = Stack()
for _ in range(n):
    control = sys.stdin.readline().replace('\n', '')
    # print(control)

    if control == 'top':
        stack.stackTop()
    elif control == 'size':
        stack.stackSize()
    elif control == 'empty':
        stack.isEmpty()
    elif control == 'pop':
        stack.pop()
    else:
        _, b = control.split()
        stack.push(int(b))
