def solution(bridge_length: int, weight: int, truck_weights: list):
    time = 0
    rest = weight

    queue = []
    passed = []

    while truck_weights or queue:
        # print(f'{time} {passed} {queue} {truck_weights}')
        if queue and time > 0 and time - queue[0][1] == bridge_length:
            passed_truck = queue.pop(0)
            passed.append(passed_truck)
            rest += passed_truck[0]
            
        if truck_weights and truck_weights[0] <= rest:
            staged_truck = truck_weights.pop(0)
            rest -= staged_truck
            queue.append((staged_truck, time))

        time += 1

    return time

print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))