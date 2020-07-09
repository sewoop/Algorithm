def solution(s):
    if s[0].isdigit():
        return int(s)
    elif s[0] == '-' :
        return int(s[1:]) * -1
    else :
        return int(s)