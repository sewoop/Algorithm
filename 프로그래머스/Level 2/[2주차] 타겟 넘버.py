answer = sumation = 0  # 방법의 수 / 합
numberList = []
targetNumber = 0

def find(index):
    global sumation, answer

    if index == len(numberList):
        if sumation == targetNumber:
            answer += 1
        return

    for i in range(2):
        if i % 2 == 0:
            sumation += numberList[index]
            find(index + 1)
            sumation -= numberList[index]

        else:
            sumation -= numberList[index]
            find(index + 1 )
            sumation += numberList[index]

def solution(numbers, target):
    global numberList, targetNumber

    numberList = numbers
    targetNumber = target

    find(0)
    return answer


## 분할 정복
def solutions(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0  
    else:
        return solutions(numbers[1:], target - numbers[0]) + solutions(numbers[1:], target + numbers[0])

numbers = [1, 1, 1, 1, 1]
target = 3
print(solutions(numbers, target))