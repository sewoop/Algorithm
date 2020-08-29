from collections import Counter
import re

test_cases = int(input())

for test_case in range(1, test_cases+1):
    card_numbers = int(input())
    card = str(input())

    # 허용하지 않는 라이브러리..
    # p = re.compile('[0-9]')

    number_list = re.findall(r'[0-9]', card)
    # print(number_list)

    count_card = Counter(number_list)
    count_card = sorted(count_card.items(), key=lambda x: (x[1], x[0]), reverse=True)

    print(f'#{test_case} {count_card[0][0]} {count_card[0][1]}')


    