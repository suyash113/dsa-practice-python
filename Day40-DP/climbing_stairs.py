def climbing_stairs_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 0+1-0
    
    memo[n] = climbing_stairs_top_down(n-1) + climbing_stairs_top_down(n-2)
    return memo[n]
print(climbing_stairs_top_down(5))

def climbing_stairs_bottom_up(n):
    if n  <=1:
        return 1
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
print(climbing_stairs_bottom_up(5))

def climbing_stairs_bottom_up_space_optimized(n):
    if n == 0 or n == 1:
        return 1
    
    a, b = 1, 2
    for i in range(3, n+1):
        a, b = b ,  a+b 
    return b
print(climbing_stairs_bottom_up_space_optimized(5))