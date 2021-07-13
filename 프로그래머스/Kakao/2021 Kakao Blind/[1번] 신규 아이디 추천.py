import re

def solution(new_id: str):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = re.sub("[^0-9a-z-_.]", "", new_id)

    # 3단계
    new_id = re.sub("\.+", ".", new_id)

    # 4단계
    new_id = re.sub("^[.]|[.]$", "", new_id)

    # 5단계, 6단계
    new_id = 'a' if len(new_id) == 0 else new_id[:15]
    new_id = re.sub("[.]$", "", new_id)

    # 7단계
    while len(new_id) <= 2: 
        new_id += new_id[-1]

    return new_id


new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = ".."
print(solution(new_id))