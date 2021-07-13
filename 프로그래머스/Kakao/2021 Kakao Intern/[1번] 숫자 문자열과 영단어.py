# 카카오 인턴쉽 2021 - 1번 문제
def solution(s: str):
    diction = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    answer = s

    # 사전에서 해당하는 글자를 replace 사용하여 변경
    for k in diction.keys():
        if k in s:
            # replace한 문자열을 answer에 덮어씌움
            answer = answer.replace(k, diction[k])

    return int(answer)
