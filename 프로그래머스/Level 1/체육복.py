def solution(n, lost, reserve):
    reserve_list = set(reserve)-set(lost)
    lost_list = set(lost)-set(reserve)

    # print(reserve_list)
    # print(lost_list)

    for i in reserve_list:
        if i-1 in lost_list:
            lost_list.remove(i-1)
        elif i+1 in lost_list:
            lost_list.remove(i+1)

    return n-len(lost_list)


if __name__ == "__main__":
    # n=5
    # lost=[2, 4]
    # reserve=[1, 3, 5]

    # n=5
    # lost=[2, 4]
    # reserve=[3]

    # n=3
    # lost=[3]
    # reserve=[1]

    # n = 5
    # lost = [1, 3]
    # reserve = [2, 4]

    # n = 5
    # lost = [3, 5]
    # reserve = [2, 4]

    # n = 8
    # lost = [2,3,4]
    # reserve = [1]

    n = 8
    lost = [5, 6]
    reserve = [4, 5]

    print(solution(n, lost, reserve))
