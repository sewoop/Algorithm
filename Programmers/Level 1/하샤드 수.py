def solution(x):
    lists = [i for i in str(x)]
    return True if int(''.join(lists))%sum(map(int, lists))==0 else False

if __name__ == "__main__":
    arr = 18
    print(solution(arr))