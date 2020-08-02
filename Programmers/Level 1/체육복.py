def solution(n, lost, reserve):
    reserve = set(reserve)-set(lost)
    lost = set(lost)-set(reserve)

    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)

    return n-len(lost)

# n=5
# lost=[2, 4]
# reserve=[1, 3, 5]

# n=5
# lost=[2, 4]
# reserve=[3]

n=3
lost=[3]
reserve=[1]

print(solution(n,lost,reserve))