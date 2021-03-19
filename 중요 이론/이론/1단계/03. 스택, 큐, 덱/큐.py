## 파이썬 리스트를 활용한 큐
class QueueInternalList(list):
    enqueue = list.append

    def dequeue(self):
        return self.pop(0)

    def isEmpty(self):
        if not self:
            return True
        else:
            return False

    def top(self):
        return self[0]



## 직접 구현한 큐
class NodeLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False

    def enqueue(self, data):
        newNode = NodeLinkedList(data)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        
        self.tail.next = newNode
        self.tail = newNode

    def dequeue(self):
        if self.isEmpty():
            return None
        
        returnData = self.head.data
        self.head = self.head.next

        return returnData

    def top(self):
        return self.tail.data

    def display(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next



if __name__ == "__main__":
    queue = QueueLinkedList()

    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.display()
    
    queue.isEmpty()
    
    print(f"top: {queue.top()}")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.display()