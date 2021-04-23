import heapq
def solution(jobs):
    answer = now = i = 0
    start = -1
    heap = []

    while i < len(jobs):
        for j in jobs:
            if j[0] in range(start + 1, now + 1):
                heapq.heappush(heap, (j[1], j[0]))
            
        if len(heap) > 0:
            curr = heapq.heappop(heap)
            start = now
            now += curr[0]
            answer += (now - curr[1])
            i += 1
        else:
            now += 1

    return answer // len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]
# jobs = [[0,4], [0,3], [0,2], [0,1]]
# jobs = [[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]
# jobs = [[0,1],[0,1],[1,0]]
# jobs = [[0, 10], [4, 10], [15, 2], [5, 11]]
print(solution(jobs))