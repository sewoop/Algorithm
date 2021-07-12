def solution(n, arr1, arr2):
    # answer = []
    # for a, b in zip(arr1, arr2):
    #     answer.append(format(a|b,'b').zfill(n).replace('1','#').replace('0b','').replace('0',' '))
    answer = [format(a | b, 'b').zfill(n).replace('1', '#').replace(
        '0b', '').replace('0', ' ') for a, b in zip(arr1, arr2)]

    # print(answer)
    return answer


if __name__ == "__main__":
    # n = 5
    # arr1 = [9, 20, 28, 18, 11]
    # arr2 = [30, 1, 21, 17, 28]

    n = 6
    arr1 = [46, 33, 33, 22, 31, 50]
    arr2 = [27, 56, 19, 14, 14, 10]

    print(solution(n, arr1, arr2))
