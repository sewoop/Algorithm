def solution(n):

    temp = []
    while True:
        if n in [1,2,3]:
            temp.append(str(n))
            break
        temp.append(str(n%3))
        n//=3
    
    return ''.join(temp[::-1]).replace('3','4')

if __name__ == "__main__":

    n = 15
    print(solution(n))