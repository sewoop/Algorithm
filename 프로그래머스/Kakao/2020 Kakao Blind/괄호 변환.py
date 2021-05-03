def solution(p):
    def isCorrect(string):
        stack = []
        for s in string:
            if s == "(":
                stack.append(s)
            elif stack and s == ")":
                stack.pop()
            else:
                return False
        return True
    
    def balance(string):
        if len(string) == 0: return "" # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        
        # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
        # 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
        cnt = 0
        for i, s in enumerate(string):
            if s == "(": cnt += 1
            else: cnt -= 1
            if cnt == 0:
                u, v = string[:i + 1], string[i + 1:]
                break
        
        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
        if isCorrect(u):
            return u + balance(v) # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        else: # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
            return "(" + balance(v) + ")" + "".join(list(map(lambda x: "(" if x == ")" else ")", u[1:-1])))

    answer = balance(p)
    return answer

p = "()))((()"
print(solution(p))