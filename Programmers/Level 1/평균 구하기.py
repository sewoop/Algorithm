# def solution(arr):
#     return int(sum(arr)/len(arr)) if (sum(arr)/len(arr)).is_integer() else sum(arr)/len(arr)

def solution(arr):
    return sum(arr)/len(arr)
if __name__ == "__main__":
    arr = [1,2,3,4]
    # arr = [5,5]

    print(solution(arr))