# import time
# start = time.time()

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Link:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, link):
        data = link.head.data

        prev = self.head
        curr = self.head
        while curr:
            if data < curr.data:
                if curr == self.head:
                    link.tail.next = curr
                    self.head = link.head
                    break
                else:
                    prev.next = link.head
                    link.tail.next = curr
                    break
            if curr == self.tail:
                curr.next = link.head
                break

            prev = curr
            curr = curr.next
            
    def add(self, data: int):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def printf(self):
        lst = []
        curr = self.head

        while curr:
            lst.append(curr.data)
            curr = curr.next
        
        print(lst)

    def print_reverse(self) -> list:
        lst = []
        curr = self.head

        while curr:
            lst.append(curr.data)
            curr = curr.next
        
        lst = lst[::-1]
        return lst[0:10]


ts = int(input())
# ts = 1

for t in range(1, ts + 1):
    N, M = map(int, input().split())
    # N, M = 4, 4

    # 메인 링크리스트
    main_link = Link()

    for i in input().split():
        main_link.add(int(i))
    
    # for i in [2, 3, 4, 5]:
    #     main_link.add(int(i))

    # 서브 링크리스트
    for _ in range(N-1):
        sub_link = Link()

        for i in input().split():
            sub_link.add(int(i))
        
        main_link.insert(sub_link)
        # del(sub_link)
        
    # main_link.printf()
    lst = main_link.print_reverse()

    print(f'#{t} {" ".join([str(i) for i in lst])}')

# print("time :", round(time.time()-start, 2))