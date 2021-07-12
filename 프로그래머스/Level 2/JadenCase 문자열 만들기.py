# sol1
def solution(s):
    string = ""
    flag = False
    for i in s:
        if i == " ":
            flag = False
        else:
            if not flag:
                flag = True
                string += i.upper()
                continue
        string += i.lower()
    return string

# sol2


def solution(s):
    return s.title()  # 개편되어 사용 불가

# sol3


def solution(s):
    return ' '.join([word.capitalize() for word in s.split(" ")])


s = "3people unFollowed me    for the last week"
print(solution(s))
