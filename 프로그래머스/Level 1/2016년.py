# 2016년 문제
import datetime


def solution(a, b):
    answer = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return answer[datetime.date(2016, a, b).weekday()]
