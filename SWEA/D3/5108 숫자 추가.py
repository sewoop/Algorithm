class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class Link:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, index: int, data: int):
        new_node = Node(data)
        
        if self.head == None:
            print("insertion is banned")
        else:
            curr = self.head
            count = 0
            while curr:
                if index == 0:
                    new_node.next = curr
                    self.head = new_node
                    curr = self.head
                    break

                if index-1 == count:
                    new_node.next = curr.next
                    curr.next = new_node
                    break
                curr = curr.next
                count += 1

    def add(self, data: int):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node        
        else:
            new_node.next = None
            self.tail.next = new_node

        self.tail = new_node

    def find(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr:
            if index == count:
                return curr.data
            
            curr = curr.next
            count += 1

    def printf(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.data)
            curr = curr.next

        print(lst)

ts = int(input())
# ts = 1

for t in range(1, ts + 1):
    N, M, L = map(int, input().split())
    # N, M, L = 5, 2, 5

    link = Link()

    for i in input().split():
        link.add(int(i))

    # print()
    # link.printf()

    for _ in range(M):
        idx, val = map(int, input().split())
        link.insert(idx, val)
        # link.printf()
    
    # link.printf()

    print(f'#{t} {link.find(L)}')
    

