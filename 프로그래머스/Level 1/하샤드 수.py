def solution(x):
    lists = [i for i in str(x)]
    return True if int(''.join(lists))%sum(map(int, lists))==0 else False

def solution(x):
    return x%sum([int(c) for c in str(x)])==0

if __name__ == "__main__":
    arr = 18
    print(solution(arr))