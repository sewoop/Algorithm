def solution(progresses: list, speeds: list) -> list:
    answer = []
    
    works = []
    stack_item = maximum = total = 0

    for progress, speed in zip(progresses, speeds):
        work_day = (100 - progress) // speed 
        if (100 - progress) % speed == 0:
            works.append(work_day)
        else:
            works.append(work_day + 1)
    
    while total != len(progresses):
        # print(f'{works} {maximum} {stack_item} {answer}')
        if stack_item == 0:
            maximum = works.pop(0)
            stack_item += 1
            continue
        
        if works and works[0] <= maximum:
            works.pop(0)
            stack_item += 1
        else:
            answer.append(stack_item)
            total += stack_item
            stack_item = maximum = 0

    return answer

# progresses=[95, 90, 99, 99, 80, 99]
# speeds=[1, 1, 1, 1, 1, 1]

# progresses = [93, 30, 55]
# speeds = [1, 30, 5]

# progresses = [97, 97, 95]
# speeds = [2, 3, 1]

# progresses = [0,0,0,0]
# speeds=[100,50,34,25]

# progresses = [5,5,5]
# speeds = [21,25,20]

# progresses = [93, 30, 55, 60, 40, 65]
# speeds = [1, 30, 5 , 10, 60, 7]

# progresses = [98,95]
# speeds = [3,1]

# progresses = [99, 1, 99, 1] 
# speeds = [1, 1, 1, 1] 

print(solution(progresses, speeds))