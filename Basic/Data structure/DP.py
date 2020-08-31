def fibo(n: int) -> int:
    global memo
    if n >= 2 and len(memo) <= 2:
        memo.append(fibo(n-1) + fibo(n-2))
    
    return memo[n]

memo = [0,1]
print(fibo(int(input())))