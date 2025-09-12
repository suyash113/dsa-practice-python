# def knapsack(weights, values,capacity):
#     W = capacity
#     m = len(weights)
    

#     dp = [[0]*(W+1) for _ in range(m+1)]

#     for i in range(m+1):
#         for w in range(W+1):
#             if weights[i-1] > w:
#                 dp[i][w] = dp[i-1][w]
#             else:
#                 dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+ values[i-1])
#     # return dp[m][w]

#     chosen_items = []
#     w = W
#     for i in range(m, 0, -1):
#         if dp[i][w] != dp[i-1][w]:
#             chosen_items.append(i-1)
#             w -= weights[i-1]
#     return dp[m][W], chosen_items[::-1] 

# weights = [1, 3, 4, 5]
# values = [1, 4, 5, 7]
# W = 7

# max_value, items = knapsack(weights, values, W)
# print("Max Value:", max_value)
# print("Items chosen:", items)       


def knapsack(weights, values, capacity):
    n = len(weights)
    W = capacity

    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]]+values[i-1])
    
    chosen_items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            chosen_items.append(i-1)
            w -= weights[i-1]
    return dp[n][W], chosen_items[::-1]

weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
W = 7

max_value, items = knapsack(weights, values, W)
print("Max Value:", max_value)
print("Items chosen:", items)    