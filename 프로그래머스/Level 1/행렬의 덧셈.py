# 일반적인 방법
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[0])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)
    return answer

# Zip을 활용
def solution(arr1,arr2):
    return [[c+d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]

if __name__ == "__main__":
    arr1 = [[1,2],[2,3]]
    arr2 = [[3,4],[5,6]]

    print(solution(arr1,arr2))