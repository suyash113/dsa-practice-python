# def unique_path(m,n):
#     dp = [[1]*n for _ in range(m)]

#     for i in range(1,m):
#         for j in range(1,n):
#             dp[i][j] = dp[i-1][j] + dp[i][j-1]
#     return dp[m-1][n-1]

# print(unique_path(3,7))

def unique_path(m, n):
    dp = [[1]*n for _ in range(m)]
    print(dp)
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
print(unique_path(3,7))



#space optimized
def unique_pth(m, n):
    dp = [1]*n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j-1]
    return dp[n-1]
print(unique_pth(3,7))