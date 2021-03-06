# import re

# compile() 정규식 패턴을 입력으로 받아 "정규식 객체"를 리턴

# search()는 처음 매칭되는 문자열만 리턴 => 객체를 반환 없으면 None 반환

# findall()는 메칭되는 모든 경우를 리턴

# group() MatchObject로부터 실제 결과 문자열을 얻는다.

# ^ : 이 패턴으로 시작해야함 ex) ^abc : abc로 시작해야함
# $ : 이 패턴으로 종료해야함 ex) abc$ : abc로 종료해야함
# [문자들] : 문자들 중 하나이어야함, 가능한 문자드르이 집합 ex) [Pp]ython : Python or python
# [^문자들] : 문자들 외의 하나이어야함
# | : 두 패턴 중 하나 이어야함
# ? : 앞 패턴이 없거나 하나이어야 함 ex) \d? : 숫자가 하나 있거나 없어야 함
# + : 앞 패턴이 하나 이상이어야 함 ex) \d+ : 숫자가 하나 이상이어야 함
# * : 앞 패턴이 0개 이상이어야 함 ex) \d* : 숫자가 없거나 하나 이상이어야 함
# 패턴{n} : 앞 패턴이 n번 반복해서 나타나는 경우 ex) \d{3} : 숫자가 3개 있어야 함
# 패턴{n, m} : 앞 패턴이 최소 n번, 최대 m번 반복해서 나타나는 경우 ex) \d{3,5} : 숫자가 3~5개 있어야함
# \d : 숫자 0-9 ex) \d\d\d : 0-9 범위의 숫자 3개를 의미
# \w : 문자를 의미
# \s : 화이트 스페이스를 의미
# . : 뉴라인(\n)을 제외한ㄴ 모든 문자를 의미 ex) .{3} : 문자 3개
