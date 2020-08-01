# 이 코드는 O(n^2)
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i]>prices[j]:
                break
            else:
                answer[i]+=1
    return answer

# 이 코드는 O(n)
def solution(prices):
    answer = [0]*len(prices)
    
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]]>prices[i]:
            top = stack.pop()
            answer[top] = i-top

        stack.append(i)

    while stack : 
        top = stack.pop()
        answer[top] = n-1-top

    return answer

# prices = [1, 2, 3, 2, 3, 3, 1]
prices = [1,2,3,2,3]
print(solution(prices))
