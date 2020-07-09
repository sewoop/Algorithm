def solution(s):
    cnt=0
    if len(s)==4 or len(s)==6:
        for i in s :
            if i.isdigit(): cnt+=1

    if cnt != len(s) : return False
    else : return True