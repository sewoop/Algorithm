from collections import deque

stack = deque()

stack.append(3)
print(stack[-1])
stack.pop()

print(stack)
print(len(stack))

stack.append(4)
print(stack)
stack.clear()
print(stack)

class StackDeque(deque):
    push = deque.append

    def is_empty(self):
        if not self:
            return True
        else:
            return False

    def top(self):
        return self[-1]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        
        ret_data = self.head.data
        self.head = self.head.next

        return ret_data

    def top(self):
        if self.is_empty():
            return None
        
        return self.head.data

if __name__ == "__main__":
    
    stack = Stack()
    stack.push(2)
    stack.push(3)
    stack.pop()

    print(stack)