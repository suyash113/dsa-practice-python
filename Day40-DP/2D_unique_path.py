def unique_path(m,n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]
print(unique_path(5,7))
print(unique_path(5,5))



def uniquePaths(m, n):
    dp = [1] * n  # only one row needed

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j-1]

    return dp[n-1]


# Example
print(uniquePaths(5,7))  # Output: 6
print(uniquePaths(5, 5))  # Output: 28
