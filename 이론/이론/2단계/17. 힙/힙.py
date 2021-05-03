class Heap(object):
    def __init__(self):
        self.queue = [None]

    def parent(self, index):
        return index // 2

    def leftChild(self, index):
        return 2 * index

    def rightChild(self, index):
        return 2 * index + 1

    def insert(self, data):
        # 맨 마지막에 삽입할 원소를 임시로 추가
        self.queue.append(data) # [None, data]
        last_index = len(self.queue) - 1 # 1

        # 부모를 타고 올라가면서 크기를 비교
        while last_index > 1:
            parent_index = self.parent(last_index)
            if self.queue[last_index] < self.queue[parent_index]:
                self.queue[last_index], self.queue[parent_index] = self.queue[parent_index], self.queue[last_index]
                last_index //= last_index
            else:
                break

    def remove(self):
        if len(self.queue) > 1:
            self.queue[1], self.queue[-1] = self.queue[-1], self.queue[1]
            data = self.queue.pop()
            self.heapify(1)
        else:
            data = None
        
        return data

    def heapify(self, index):
        left = self.leftChild(index)
        right = self.rightChild(index)

        smallest = index

        # 왼쪽 자식이 존재하는 지, 그리고 왼쪽 자식의 값이 더 큰 지를 판단.
        if left < len(self.queue) and self.queue[smallest] > self.queue[left]:
            # 조건이 만족하는 경우, smallest는 왼쪽 자식의 인덱스를 갖는다.
            smallest = left
        # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 값이 더 큰 지를 판단.
        if right < len(self.queue) and self.queue[smallest] > self.queue[right]:
            # 조건을 만족하는 경우, smallest는 오른쪽 자식의 인덱스를 가진다.
            smallest = right

        if smallest != index:
            # 현재 노드와 최댓값 노드를 교체
            self.queue[index], self.queue[smallest] = self.queue[smallest], self.queue[index]
            # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리한다.
            self.heapify(smallest)


heap = Heap()
heap.insert(5)
heap.insert(1)
heap.insert(2)
heap.insert(4)
heap.insert(3)
heap.insert(6)
heap.insert(8)

print(heap.queue)

result = []
for _ in range(len(heap.queue) - 1):
    result.append(heap.remove())

print(result)

# ------------------------------------------------------

# 내장함수 heapq
import heapq
heaps = []
heapq.heappush(heaps, 5)
heapq.heappush(heaps, 1)
heapq.heappush(heaps, 2)
heapq.heappush(heaps, 4)
heapq.heappush(heaps, 3)
heapq.heappush(heaps, 6)
heapq.heappush(heaps, 8)

print(heaps)

heapq.heapify

result1 = []
for _ in range(len(heaps)):
    v = heapq.heappop(heaps)
    result1.append(v)

print(result1)