# def unique_path_obstcl(grid):
#     m = len(grid)
#     n = len(grid[0])
#     dp = [[0]*n for _ in range(m)]
#     dp[0][0] = 1
#     for i in range(1,m):
#         if grid[i][0] == 0:
#             dp[i][0] = dp[i-1][0]
#     for j in range(1,n):
#         if grid[0][j] == 0:
#             dp[0][j] = dp[0][j-1]
    
#     for i in range(1, m):
#         for j in range(1, n):
#             if grid[i][j] != 1: #and grid[i-1][j] != 1 and grid[i][j-1] != 1:
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
#     return dp[m-1][n-1]
# print(unique_path_obstcl([[0,0,0],[0,1,0],[0,0,0]]))
# print(unique_path_obstcl([[0,1],[0,0]]))


def unique_path_obs(grid):
    m = len(grid)
    n = len(grid[0])

    if grid[0][0] ==1 or grid[m-1][n-1] == 1:
        return 0 
    
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1
    for i in range(1,m):
        if grid[i][0] ==0:
            dp[i][0] = dp[i-1][0]
    
    for j in range(1,n):
        if grid[0][j] == 0:
            dp[0][j] = dp[0][j-1]
    print(dp)
    for i in range(1,m):
        for j in range(1,n):
            if grid[i][j] == 0:
                a = dp[i-1][j]
                b = dp[i][j-1]
                dp[i][j] = a + b
    return dp[m-1][n-1]
print(unique_path_obs([[0,0,0],[0,1,0],[0,0,0]]))
# print(unique_path_obs([[0,1],[0,0]]))


def unique_path_obst(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [0]*n
    dp[0] = 1
    for j in range(1,n):
        if grid[0][j] == 0:
            dp[j] = dp[j-1]

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 1:
                dp[j] = 0
            elif j > 0  :
                dp[j] += dp[j-1]
    return dp[n-1]
# print(unique_path_obst([[0,0,0],[0,1,0],[0,0,0]]))