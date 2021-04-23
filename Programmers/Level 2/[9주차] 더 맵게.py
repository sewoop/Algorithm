import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # heapify를 안해주면 [1, 0]일때 heappop을 하면 0이 아닌 1이 나온다.

    while True:
        lowest = heapq.heappop(scoville)
        if lowest >= K:
            return answer

        if len(scoville) == 0:
            return -1

        two_low = heapq.heappop(scoville)

        heapq.heappush(scoville, lowest + (two_low * 2))
        answer += 1

# scoville = [1, 2, 3, 19, 10, 12]
# scoville = [2, 3, 7, 10, 15]
# K = 7

scoville = [1, 0]
K = 1

print(solution(scoville, K))