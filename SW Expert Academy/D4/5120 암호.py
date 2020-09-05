class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class Link:
    def __init__(self):
        self.head = None
        self.tail = None
        self.temp = None

    def add(self, data: int):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node
        self.temp = self.head

        # 원순열로 변경
        self.tail.next = self.head
        self.head.prev = self.tail

    def insert(self, index: int):
        curr = self.temp
        count = 0
        while curr:
            if count == index:
                prev = curr.prev
                data = prev.data + curr.data
                new_node = Node(data)

                # [6, 2, 4, 13, 9, 1, 5]
                # [6, 2, 4, 13, 9, 1, 6, 5]
                # [6, 8, 2, 4, 13, 9, 1, 6, 5]
                prev.next = new_node
                new_node.prev = prev
                new_node.next = curr
                curr.prev = new_node

                self.temp = new_node
                break

            curr = curr.next
            count += 1

    def printf(self):
        lst = []
        curr = self.head
        
        for _ in range(N+K):
            lst.append(str(curr.data))
            curr = curr.next

        # print(lst)
        # print(lst[::-1])
        return lst[::-1]


ts = int(input())

for t in range(1, ts + 1):
    N, M, K = map(int, input().split())

    link = Link()
    for i in input().split():
        link.add(int(i))
   
    for i in range(K):
        link.insert(M)

    lst = link.printf()
    if len(lst) >= 10:
        lst = lst[0:10]
    print(f'#{t} {" ".join(lst)}')
