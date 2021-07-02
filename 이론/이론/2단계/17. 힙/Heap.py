import heapq


# min heap
class Heap(object):
    def __init__(self):
        self.__queue = []

    # getter
    def get_queue(self):
        return self.__queue

    def __parent(self, index: int):
        return index // 2

    def __left_child(self, index: int):
        return index * 2

    def __right_child(self, index: int):
        return index * 2 + 1

    def __swap(self, lhs: int, rhs: int):
        self.__queue[lhs], self.__queue[rhs] = self.__queue[rhs], self.__queue[lhs]

    def __heapify(self, index: int):
        smallest = index
        left = self.__left_child(index)
        right = self.__right_child(index)

        # 왼쪽 자식이 존재하는 지, 그리고 왼쪽 자식의 값이 더 큰 지를 판단.
        if left < len(self.__queue) and self.__queue[left] < self.__queue[smallest]:
            # 조건이 만족하는 경우, smallest는 왼쪽 자식의 인덱스를 갖는다.
            smallest = left

        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 값이 더 큰 지를 판단.
        if right < len(self.__queue) and self.__queue[right] < self.__queue[smallest]:
            # 조건을 만족하는 경우, smallest는 오른쪽 자식의 인덱스를 가진다.
            smallest = right

        if index != smallest:
            # 현재 노드와 최댓값 노드를 교체 후
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리한다.
            self.__swap(index, smallest)
            self.__heapify(smallest)

    def insert(self, data):
        # 맨 마지막에 삽입할 원소를 임시로 추가
        self.__queue.append(data)

        # 부모를 타고 올라가면서 크기를 비교
        last_index = len(self.__queue) - 1
        while last_index > 0:
            parent_index = self.__parent(last_index)
            if self.__queue[parent_index] > self.__queue[last_index]:
                self.__swap(parent_index, last_index)
                last_index //= 2
            else:
                break

    def remove(self):
        if self.__queue:
            self.__swap(0, -1)
            data = self.__queue.pop()
            self.__heapify(0)
        else:
            data = None
        return data


heap = Heap()

heap.insert(6)
heap.insert(2)
heap.insert(8)
heap.insert(5)
heap.insert(3)
heap.insert(9)
heap.insert(1)
heap.insert(10)
heap.insert(7)
heap.insert(4)

print(heap.get_queue())

result = []
for _ in range(len(heap.get_queue())):
    result.append(heap.remove())

print(result)

# ------------------------------------------------------

# 내장함수 heapq
heaps = []

heapq.heappush(heaps, 6)
heapq.heappush(heaps, 2)
heapq.heappush(heaps, 8)
heapq.heappush(heaps, 5)
heapq.heappush(heaps, 3)
heapq.heappush(heaps, 9)
heapq.heappush(heaps, 1)
heapq.heappush(heaps, 10)
heapq.heappush(heaps, 7)
heapq.heappush(heaps, 4)

print(heaps)

result_ = []
for _ in range(len(heaps)):
    v = heapq.heappop(heaps)
    result_.append(v)

print(result_)
