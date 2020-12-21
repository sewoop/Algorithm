# 파이썬 기본 스택 구현

## 파이썬 기본 내장 리스트 사용
class StackInternalList(list):
    push = list.append

    def isEmpty(self):
        if not self:
            return True
        else:
            return False

    def top(self):
        return self[-1]
        

## 연결리스트 사용 
class NodeLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    # def __del__(self):
    #     print(f"{self} 소멸")

class StackLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False

    def push(self, data):
        newNode = NodeLinkedList(data)

        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.isEmpty():
            return None
        
        returnData = self.head.data
        self.head = self.head.next

        return returnData

    def top(self):
        if self.isEmpty():
            return None
        return self.head.data

    def display(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
            

if __name__ == "__main__":
    stack = StackLinkedList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.push(9)

    print(stack.top())
    print(stack.pop())
    print("---------")

    stack.display()