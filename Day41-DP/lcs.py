# def longest_common_subsequence(str1, str2):
#     m = len(str1)
#     n = len(str2)
#     dp = [[0]*(n+1) for _ in range(m+1)]
    
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if str1[i-1] == str2[j-1]:
#                 dp[i][j] = 1 + dp[i-1][j-1] 
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#     return dp[m][n]
# print(longest_common_subsequence("abcde", "abef"))


def longest_common_subsequence(str1, str2):
    m, n = len(str1), len(str2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
print(longest_common_subsequence("abe", "abef"))


