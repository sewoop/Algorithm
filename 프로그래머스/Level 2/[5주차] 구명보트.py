from collections import deque

# 실패 (효율성 평가도 실패)
def solution_nope(people, limit):
    ''' 조건
    구명보트 하나 당 최대 2명
    제한을 넘기면 안됨
    '''

    answer = 0
    people.sort(reverse=True) # 몸무게가 큰 것부터 정렬
    
    total = len(people) # 총 사람 수
    ride = [0] * total # 탑승 여부를 확인

    for i in range(total):
        if ride[i] == 0: # 만약, 탑승하지 않은 상태면 진행
            temp = limit - people[i] # 최대 탑승 무게에서 뺀 것
            ride[i] = 1 # 탑승 상태로 기록
            for j in range(i + 1, total): # 이후의 사람들 중 남은 무게에 해당하는 사람이 있는 지를 탐색
                if people[j] <= temp: # 만족하면
                    ride[j] = 1 # 탑승 상태로 기록하고
                    break # 탐색 종료 (최대 탑승 인원이 2명이기 때문)
            answer += 1 # 그리고 +1를 해준다.
                
    return answer

# deque을 이용한 풀이
def solution(people, limit):
    answer = 0
    people.sort(reverse=True) # 내림차순으로 정렬
    # [80, 70, 50, 50]

    queue = deque(people) # deque을 이용하여 양방향 큐를 구현

    while queue: # 큐가 있는 동안
        if limit - queue[0] >= queue[-1]: # 최대 무게에서 좌측(큰 무게)를 빼고 남은 것을 수용할 수 있으면
            queue.pop() # 뒤에 인원을 같이 탑승 시키고

        if len(queue) > 0: # index out of range 에러 방지
            queue.popleft() # 좌측 인원은 무게가 얼마가 되든 무조건 들어간다.
        answer += 1 # 보트의 개수 +1

    return answer

if __name__ == '__main__':
    people, limit = [70, 50, 80, 50], 100
    # people, limit = [70, 80, 50], 100
    # people, limit = [40, 40, 40], 100
    print(solution(people, limit))