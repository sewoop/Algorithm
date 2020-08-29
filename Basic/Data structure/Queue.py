from collections import deque

queue = deque()

queue.append(3)
queue.append(4)
queue.append(5)
print(queue)

queue.popleft()
print(queue)

class QueueDeque(deque):
    push = deque.append
    pop = deque.popleft

    def is_empty(self):
        if not self:
            return True
        else:
            return False

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if not self.head:
            return True
        return False

    def push(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if self.is_empty():
            return None

        ret_data = self.head.data
        self.head = self.head.next
        return ret_data

if __name__ == "__main__":
    # Queue = QueueDeque()
    Queue = Queue()

    Queue.push(3)
    Queue.push(4)
    Queue.push(5)
    print(Queue)
    
    Queue.pop()
    print(Queue)