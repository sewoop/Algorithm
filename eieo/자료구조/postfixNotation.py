mathematicalExpression = "(2+5)*3*(2+1)"
# mathematicalExpression = input("Input Mathematical Expression: ")

## 단방향 연결리스트 (스택)
class NodeLinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

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
            print(curr.data, end=' ')
            curr = curr.next

operator = StackLinkedList()
result = []

priority = {
    "(":0,
    ")":0,
    "+":1,
    "-":1,
    "*":2,
    "/":2
}


for i in mathematicalExpression:
    if i == "(":
        operator.push(i)
    elif i in "*/+-":
        if operator.isEmpty():
            operator.push(i)
        
        else:
            if priority[operator.top()] >= priority[i]:
                result.append(operator.pop())
                operator.push(i)
            else:
                operator.push(i)
    elif i == ")":
        while True:
            temp = operator.pop()
            if temp == "(":
                break
            result.append(temp)

    else:
        result.append(i)
    
    operator.display()
    print(f"\nres: {result}")
            
while not operator.isEmpty():
    result.append(operator.pop())

print(''.join(result))