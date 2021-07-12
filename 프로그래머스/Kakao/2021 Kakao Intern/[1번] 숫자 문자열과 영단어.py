def solution(s: str):
    diction = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    }
    answer = s

    for k in diction.keys():
        if k in s:
            answer = answer.replace(k, diction[k])

    return int(answer)
