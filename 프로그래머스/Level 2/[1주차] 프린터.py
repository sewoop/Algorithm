def solution(priorities, location):
    answer = 0

    prior = sorted(priorities)
    documents = [(i, v) for i, v in enumerate(priorities)]

    lst = []

    while prior:
        maximum = max(prior)
        for index, document in enumerate(documents):
            if document[1] == maximum:
                documents = documents[index:] + documents[:index]
                break

        lst.append(documents.pop(0))
        prior.pop()

    for i, v in enumerate(lst):
        if v[0] == location:
            answer = i + 1
            break

    return answer


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
