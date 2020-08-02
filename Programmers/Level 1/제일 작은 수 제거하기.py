def solution(arr):
    arr.remove(min(arr))
    return [-1] if len(arr)==0 else arr

if __name__ == "__main__":
    # arr = [4,3,2,1]
    arr = [10]
    print(solution(arr))