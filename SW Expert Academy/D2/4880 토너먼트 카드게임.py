Ts = int(input())

def winner(left, right):
    player1 = card_number[left-1]
    player2 = card_number[right-1]
    win = ''

    # 가위(1) < 바위(2) < 보(3) < 가위 ..
    if player1 < player2:
        if player1 == 1 and player2 == 3:
            win = left
        else:
            win = right
    elif player2 < player1:
        if player2 == 1 and player1 == 3:
            win = right
        else:
            win = left
    else:
        win = left
    
    return win

# ex) tournament(1, 4): 1 2 3 4
def tournament(start, end):
    # start: 1, end: 4
    mid = (start + end)//2  # start: 1, end: 4 -> mid: 2

    if start == end:
        return start
    
    left = tournament(start, mid)  # 1, 2
    right = tournament(mid+1, end) # 3, 4

    return winner(left, right)
    

for T in range(1, Ts + 1):
    N = int(input())  # ex) 4
    card_number = [int(n) for n in list(input().split())]  # ex) [1, 3, 2, 1]

    try:
        result = tournament(1, N)  # tournament(1, 4): 1 2 3 4
    except:
        result = 'error'
        
    print(f'#{T} {result}')
