lines = int(input())

for line in range(1, lines+1):
    # 한번 충전 최대거리, 목적지, 충전 정류소 개수
    max_distance, destination, charge_stops = map(int, input().split())
    
    # 충전 정류소 넘버
    charge_stop = list(map(int, input().split()))
    
    position = 0
    count = 0
    out_of_distance = False
    match_destination = False

    while True:
        temp = 0
        for i in range(1, max_distance+1):
            if temp < position + i and position + i in charge_stop:
                temp = position + i
            
            if position+i == destination:
                match_destination = True
                break

        if match_destination:
            break

        if temp == 0:
            out_of_distance = True
            break

        else:
            position = temp
            count+=1
            
    if out_of_distance:
        count = 0
        
    # 1 3 5 7 9 : 1 3 .. 9            
    print(f'#{line} {count}')