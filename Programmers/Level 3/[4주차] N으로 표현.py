def solution(N, number):
    possible = [0, [N]] # 가능한 케이스를 전부 넣기 위한 리스트

    if N == number: # N과 number가 같으면 1개만 써도 됨
        return 1
    
    for i in range(2, 9): # 8까지 
        case = [] # N이 i개일때의 케이스를 담기 위한 리스트

        base = int(str(N) * i) # N을 i개 써서 만드는 경우 ex) 555, 5555, 55555
        case.append(base) # 케이스에 등록

        for idx in range(1, i // 2 + 1): # N의 개수를 맞추기 위해 사용 N이 1이고, number가 1121인 경우 -> 1111 + 11 - 1 = 1121로 7개이지만, 개수를 안 맞춰주면 5나 -1이 나옴
            for x in possible[idx]: # i가 3일때, f(1)과 f(3 - 1) => 즉, f(3) = f(2) + f(1)로 구성
                for y in possible[i - idx]: # 사칙 연산을 진행
                    case.append(x + y)
                    case.append(x - y)
                    case.append(y - x)
                    case.append(x * y)
                    if y != 0:
                        case.append(x / y)
                    if x != 0:
                        case.append(y / x)
            if number in case:
                return i
            possible.append(case)
    return -1

if __name__ == '__main__':
    # N, number = 5, 12
    # N, number = 2, 11
    N, number = 1, 1121

    print(solution(N, number))