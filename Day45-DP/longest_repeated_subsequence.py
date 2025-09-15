def longest_repeated_subsequence(s):
    n = len(s)
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # print(dp)
    i,j = n,n
    lrs = []
    while i > 0 and j > 0:
        if s[i-1] == s[j-1] and i != j:
            lrs.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(lrs)), dp[n][n]

# Test
s = "ATAKTKGGA" #"aaabbbcccdddeeffgg"aaabbbcccdddeeffgg aabbccddg
print("Longest Repeated Subsequence:", longest_repeated_subsequence(s))