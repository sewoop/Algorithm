diction = {
    "apple": 1,
    "banana": 3,
    "melon": 2
}

print(sorted(diction)) # default는 key값을 기준으로 정렬한다.

# value값을 기준으로 정렬하기
print(sorted(diction, key=lambda k: diction[k]))

# tuple로 된 형식
print(diction.items())

# tuple 형식의 key 기준 정렬
print(sorted(diction.items())) # key값을 기준으로 정렬됨

# tuple 형식의 value 기준 정렬
print(sorted(diction.items(), key=lambda k: k[1])) # k = (key, value) => k[1] == value