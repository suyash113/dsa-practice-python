def house_robber(homes):
    n = len(homes)
    if n == 0:
        return 0
    if n == 1:
        return homes[0]
    dp = [0]*n
    dp[0] = homes[0]
    dp[1] = max(homes[0], homes[1])

    for i in range(2,n):
        dp[i] = max(dp[i-1], homes[i]+dp[i-2])
    return dp[n-1]
print(house_robber([2, 7, 9, 3, 1]))



def house_robber(homes):
    n = len(homes)
    prev1, prev2 = 0, 0

    for num in homes:
        curr = max(prev1, prev2+num)
        prev2, prev1 = prev1, curr
    return prev1
print(house_robber([2, 7, 9, 3, 1]))