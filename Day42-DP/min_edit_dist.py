def min_edit_dist(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        dp[i][0] = 1 + dp[i-1][0]
    
    for j in range(1, n+1):
        dp[0][j] = 1 + dp[0][j-1]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    return dp[m][n]

print(min_edit_dist("intention", "execution")) 

