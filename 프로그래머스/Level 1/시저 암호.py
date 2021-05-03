def solution(s, n):
    answer = ''
    
    for char in s:
        k = ord(char)
        if k==32:
            answer+=chr(k)
            continue
        
        if k in range(65,91):
            k = k+n
            if k>90:
                k=k-(26)

        elif k in range(97,123):
            k = k+n
            if k>122:
                k=k-(26)
        
        answer+=chr(k)

    return answer

if __name__ == "__main__":
    # s = "AaZz"
    # n = 25

    # s = "AB"
    # n = 1

    # s = "z"
    # n = 1

    s = "a B z"
    n = 4


    print(solution(s,n))