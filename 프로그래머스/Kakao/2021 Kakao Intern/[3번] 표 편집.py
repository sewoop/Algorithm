# 카카오 인턴쉽 2021 - 3번 문제
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Niniz:
    def __init__(self, n):
        self.__base = ['X'] * n
        self.__stack = []
        self.__cursor = None
        self.__head = None
        self.__tail = None

    # 기존 상태와 다른 것을 찾아 결과값을 반환
    def res(self):
        curr = self.__head
        while curr:
            self.__base[curr.data] = 'O'
            curr = curr.next
        return ''.join(self.__base)

    def add(self, data, k):
        new_node = Node(data)

        if data == k:
            self.__cursor = new_node

        if not self.__head:
            self.__head = new_node
            self.__tail = new_node
            return

        new_node.prev = self.__tail
        self.__tail.next = new_node
        self.__tail = new_node

    def up(self, num):
        for _ in range(num):
            if self.__cursor.prev:
                self.__cursor = self.__cursor.prev

    def down(self, num):
        for _ in range(num):
            if self.__cursor.next:
                self.__cursor = self.__cursor.next

    def cut(self):
        # Restore을 위하여 stack에 저장
        self.__stack.append(self.__cursor)

        # Case 1. 현재 커서 앞에 노드가 있지만 뒤에는 없는 경우 (= 맨 뒤의 경우)
        if self.__cursor.prev and not self.__cursor.next:
            self.__cursor.prev.next = None
            self.__tail = self.__cursor.prev
            self.__cursor = self.__cursor.prev

        # Case 2. 현재 커서 앞에 노드가 없지만 뒤에는 있는 경우 (= 맨 앞의 경우)
        elif not self.__cursor.prev and self.__cursor.next:
            self.__cursor.next.prev = None
            self.__head = self.__cursor.next
            self.__cursor = self.__cursor.next

        # Case 3. 둘다 있는 경우 (= 노드 사이의 경우)
        elif self.__cursor.prev and self.__cursor.next:
            self.__cursor.prev.next = self.__cursor.next
            self.__cursor.next.prev = self.__cursor.prev
            self.__cursor = self.__cursor.next

        # Case 4. 둘다 없는 경우 (= 현재 1개 밖에 남아있지 않은 상태)
        else:
            self.__head = None
            self.__tail = None
            self.__cursor = None

    def restore(self):
        node = self.__stack.pop()

        # 각각 if문을 해주어 앞 노드가 없으면 뒷 노드만, 뒷 노드가 없으면 앞 노드만, 둘다 있으면 둘다 연결
        # 꺼냈던 노드가 삭제 전에 앞에 노드가 있었던 경우
        if node.prev:
            if node.prev == self.__tail:
                self.__tail = node
            node.prev.next = node

        # 꺼냈던 노드가 삭제 전에 뒤에 노드가 있었던 경우
        if node.next:
            if node.next == self.__head:
                self.__head = node
            node.next.prev = node


def solution(n, k, cmd):
    niniz = Niniz(n)

    # 연결 리스트 데이터 생성
    for i in range(n):
        niniz.add(i, k)

    for c in cmd:
        if "U" in c:
            _, num = c.split()
            niniz.up(int(num))
        elif "D" in c:
            _, num = c.split()
            niniz.down(int(num))
        elif "C" in c:
            niniz.cut()
        elif "Z" in c:
            niniz.restore()

    return niniz.res()


# n, k, cmd = 8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
n, k, cmd = 8, 2, ["D 2", "C", "U 3", "C",
                   "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
# n, k, cmd = 5, 2, ["U 2", "C", "D 3"]
print(solution(n, k, cmd))
