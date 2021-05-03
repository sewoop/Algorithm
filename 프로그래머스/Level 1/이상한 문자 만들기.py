def solution(s):
    answer = ''

    index = 0
    for char in s:
        if ord(char)==32:
            answer+=char
            index = 0
            continue
            
        if index%2==0:
            char = char.upper()
        else:
            char = char.lower()
        index+=1
        answer+=char

    return answer

if __name__ == "__main__":
    s = "AAAAAAAAAAA A A A A     AAAAA AAA"
    print(solution(s))