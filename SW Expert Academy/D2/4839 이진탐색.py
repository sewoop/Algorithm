Ts = int(input())

def search(find: int, end: int) -> int:
    '''
        find: 찾아야하는 페이지 넘버
        end: 책의 마지막 페이지
    '''
    start = 1
    count = 0
    center = 0

    while True:
        count+=1
        center = int((start + end)/2)

        if center < find:
            start = center
            continue
        elif center > find:
            end = center
            continue
        else:
            break

    return count

for T in range(1, Ts + 1):
    end, A, B = map(int, input().split())

    A_ = search(A, end)
    B_ = search(B, end)

    if A_ < B_:
        win = 'A'
    elif A_ > B_:
        win = 'B'
    else:
        win = 0

    print(f'#{T} {win}')








    