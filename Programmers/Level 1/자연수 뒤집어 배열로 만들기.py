def solution(n):
    return [int(i) for i in list(reversed(str(n)))]

if __name__ == "__main__":
    n = 12345
    print(solution(n))