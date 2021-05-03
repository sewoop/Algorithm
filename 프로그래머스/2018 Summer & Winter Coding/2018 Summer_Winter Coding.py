def solution(d, budget):
    sum_ = 0
    for i,v in enumerate(sorted(d)):
        sum_ += v
        if sum_ > budget:
            return i
    return i+1

if __name__ == "__main__":
    # d = [1,3,2,5,4]
    # budget = 9

    # d = [2,2,3,3]
    # budget = 10

    # d = [1,2,6,9]
    # budget = 9

    d = [1,2,5]
    budget = 9

    print(solution(d,budget))