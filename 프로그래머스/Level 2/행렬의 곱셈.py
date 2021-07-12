def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for k in range(len(arr2[0])):
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                answer[i][k] += arr1[i][j] * arr2[j][k]
    return answer


def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]


arr2 = [[1, 2], [3, 4], [5, 6]]
# arr2 = [[3, 3], [3, 3]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(list(zip(*arr2)))
