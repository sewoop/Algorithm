class Node:
    def __init__(self, data: int):
        self.prev = None
        self.data = data
        self.next = None

class Link:
    def __init__(self):
        self.head = None
        self.tail = None

    # linked-list 생성
    def add(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        
        self.tail = new_node

    # method
    def insert(self, method: str, index: int, *data: int):
        curr = self.head        
        count = 0
        # method가 I 2 7: 2번 인덱스 앞에 7을 추가하고, 한 칸 씩 뒤로 이동한다
        if method == 'I':
            while curr:
                if index == 0:
                    new_node = Node(data[0])
                    curr.prev = new_node
                    new_node.next = curr
                    self.head = new_node
                    break

                if count == index:
                    new_node = Node(data[0])
                    curr.prev.next = new_node
                    new_node.prev = curr.prev

                    curr.prev = new_node
                    new_node.next = curr
                    break
                curr = curr.next
                count += 1


        # method가 D 4: 4번 인덱스 자리를 지우고, 한 칸 씩 앞으로 이동한다.
        elif method == 'D':
            while curr:
                if index == 0:
                    curr.next.prev = None
                    self.head = curr.next
                    del(curr)
                    break

                if count == index:
                    if curr.next != None:
                        curr.next.prev = curr.prev
                        curr.prev.next = curr.next
                        del(curr)
                        break
                    else:
                        curr.prev.next = None
                        self.tail = curr.prev
                        del(curr)
                        break
                    
                curr = curr.next
                count += 1

        # method가 C 3 8: 3번 인덱스 자리를 8로 바꾼다.
        else:
            while curr:
                if count == index:
                    curr.data = data[0]
                    break
                curr = curr.next
                count += 1

    def printf(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.data)
            curr = curr.next

        # print(lst)
        return lst

ts = int(input())

for t in range(1, ts + 1):
    N, M, L = map(int, input().split())

    link = Link()

    # 인덱스 수열
    for i in input().split():
        link.add(int(i))
    # link.printf()  # 체크

    # 편집
    for _ in range(M):
        inp = [i for i in input().split()]
        if len(inp) == 2:
            link.insert(inp[0], int(inp[1]))
        else:
            link.insert(inp[0], int(inp[1]), int(inp[2]))
        # link.printf()  # 체크

    result = link.printf()  # 체크
    
    try:
        print(f'#{t} {result[L]}')
    except IndexError:
        print(f'#{t} -1')