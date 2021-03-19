import time
# LinkedList의 종류 (스택, 큐)

## 단방향 연결리스트 (스택)
class OneDirectionNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class OneDirectionLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False
    
    # Stack
    def push(self, data):
        newNode = OneDirectionNode(data)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return

        newNode.next = self.head
        self.head = newNode       

    def pop(self):
        if self.isEmpty():
            return None

        returnData = self.head.data
        self.head = self.head.next

        return returnData

    def top(self):
        return self.head.data

    def display(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next
    

## 양방향 연결리스트 (스택, 큐 통합)
class DoubleDirectionNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleDirectionLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False

    # 스택
    def push(self, data):
        newNode = DoubleDirectionNode(data)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        
        # 앞에 있는 것이 새로운 노드가 되도록 설계
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode    

    def pop(self):
        if self.isEmpty():
            return None

        returnData = self.head.data
        self.head.prev = None
        self.head = self.head.next

        return returnData

    def top(self):
        return self.head.data

    # 큐
    def enqueue(self, data):
        newNode = DoubleDirectionNode(data)
        
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def dequeue(self):
        if self.isEmpty():
            return None

        returnData = self.tail.data

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev

        return returnData

    def display(self):
        curr = self.head

        while curr:
            print(curr.data)
            curr = curr.next

## 원형 단방향 연결리스트
class CircularLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    def push(self, data):
        newNode = CircularLinkedListNode(data)
        self.size += 1

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            return

        newNode.next = self.head
        self.tail.next = newNode
        self.head = newNode

    def popFirst(self): # 가장 먼저 들어온 노드를 제거
        self.size -= 1
        if self.isEmpty():
            return None

        if self.head == self.tail:
            returnData = self.head.data
            self.head = None
            self.tail = None
        else:
            curr = self.head
            while curr.next != self.tail:
                curr = curr.next

            returnData = curr.next.data
            curr.next = self.head
            self.tail = curr

        return returnData

    def popLast(self): # 가장 나중에 들어온 노드를 제거
        self.size -= 1
        if self.isEmpty():
            return None

        if self.head == self.tail:
            returnData = self.head.data
            self.head = None
            self.tail = None
        else:
            returnData = self.head.data
            self.tail.next = self.head.next
            self.head = self.head.next

        return returnData

    def display(self):
        curr = self.head
        if self.isEmpty():
            print("Empty")

        for _ in range(self.size):
            print(curr.data, end=' ')
            curr = curr.next

    def displayInfinite(self): # warning
        curr = self.head

        while True:
            print(curr.data, end=" ")
            curr = curr.next

if __name__ == "__main__":
    circule = CircularLinkedList()
    circule.push(1)
    circule.push(2)
    circule.push(3)
    circule.push(4)
    circule.push(5)
    circule.push(6)
    circule.displayInfinite()
