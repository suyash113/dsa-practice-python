def fib_top_down(n, memo={}):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_top_down(n-1) + fib_top_down(n-2)
    return memo[n]
print(fib_top_down(5))