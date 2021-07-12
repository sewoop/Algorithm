def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:  # 좌측 모서리 부분은 부모 노드의 좌측 모서리 값에서 자신을 더한 것이다.
                triangle[i][j] += triangle[i - 1][j]
            elif j == i:  # 우측 모서리 부분은 부모 노드의 우측 모서리 값에서 자신을 더한 것이다.
                triangle[i][j] += triangle[i - 1][j - 1]
            else:  # 좌,우측 모서리가 아닌 곳은 양쪽 부모와 자신의 각각의 합중에 더 큰 값을 가진다.
                triangle[i][j] += max(triangle[i - 1]
                                      [j - 1], triangle[i - 1][j])

    return max(triangle[-1])  # 리프에서 가장 큰 값을 출력


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
