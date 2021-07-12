# Linked List

# ---------------------------------------

# 단일 연결 리스트
class SingleNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # 삽입
    def insert(self, data, at):
        # at이 크기보다 클때
        if at > self.size:
            return False

        newData = SingleNode(data)

        # 리스트에 노드가 하나도 없을 때
        if not self.head:
            self.head = newData
            self.tail = newData
            self.size += 1
            return

        # 리스트에 노드가 한 개이상 있을때
        index = 0
        curr = self.head
        while curr:
            if index == at - 1:
                break
            curr = curr.next
            index += 1

        newData.next = curr.next
        curr.next = newData
        curr = newData
        self.size += 1

    # 추가
    def append(self, data):
        newData = SingleNode(data)

        # 리스트에 노드가 하나도 없을 때
        if not self.head:
            self.head = newData
            self.tail = newData
            self.size += 1
            return
        
        # 리스트에 노드가 한 개이상 있을때
        newData.next = self.tail.next
        self.tail.next = newData
        self.tail = newData
        self.size += 1

    # 삭제
    def remove(self, data):
        if not self.head:
            return False

        curr = self.head
        prev = None
        while curr:
            if curr.data == data:
                if curr == self.head:
                    self.head = curr.next
                    del curr
                    curr = self.head
                else:
                    prev.next = curr.next
                    del curr
                    curr = prev.next
                # print(self)
                return True
            prev = curr
            curr = curr.next
        return False

    # 읽기
    def __str__(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.data)
            curr = curr.next
        return f'{lst}'

    # 찾기
    def find(self, data):
        pass

if __name__ == '__main__':
    lst = SingleLinkedList()
    lst.append(4)
    lst.append(3)
    lst.append(5)
    lst.append(7)
    print(lst)
    lst.insert(data=1, at=1) # 4 1 3 5 7
    lst.insert(data=6, at=4) # 4 1 3 5 6 7
    print(lst)
    lst.remove(5)
    lst.remove(7)
    lst.remove(4)
    lst.remove(1)
    lst.remove(6)
    lst.remove(3)
    print(lst)

# ---------------------------------------

# 이중 연결 리스트
class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 삽입
    def insert(self, data):
        pass

    # 삭제
    def remove(self, data):
        pass

    # 읽기
    def __str__(self):
        pass

    # 찾기
    def find(self, data):
        pass

# ---------------------------------------

# 원형 연결 리스트
class CircularNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.next = None

    # 삽입
    def insert(self, data):
        pass

    # 삭제
    def remove(self, data):
        pass

    # 읽기
    def __str__(self):
        pass

    # 찾기
    def find(self, data):
        pass