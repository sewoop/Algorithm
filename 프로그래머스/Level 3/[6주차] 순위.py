from collections import Counter

# Floyd-warshall


def solution(n, results):
    answer = 0
    matches = [[0] * n for _ in range(n)]

    for a, b in results:
        matches[a - 1][b - 1] = 1
        matches[b - 1][a - 1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matches[i][j] == 0:  # 승패 결과가 안 정해진 것들을 정함
                    if matches[i][k] == 1 and matches[k][j] == 1:  # i > k, k > j 이면 i > j 임
                        matches[i][j] = 1
                    if matches[i][k] == -1 and matches[k][j] == -1:  # i < k, k < j 이면 i < j 임
                        matches[i][j] = -1

    for match in matches:
        if Counter(match)[0] == 1:
            answer += 1

    return answer


# n, results = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
# n, results = 8, [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]]
# n, results = 5, [[1, 4], [4, 2], [2, 5], [5, 3]]
print(solution(n, results))

'''
'''
