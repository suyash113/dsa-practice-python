def fib_bottom_up(n):
    if n <= 1:
        return n
    
    dp = [0]* (n+1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(fib_bottom_up(5))


# bottom-up but space optimized
def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b
print(fib(5))

def normal_fib(n):
    if n<=1 :
        return n
    return normal_fib(n-1) + normal_fib(n-2)
print(normal_fib(5))