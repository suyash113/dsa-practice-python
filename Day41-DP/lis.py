def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1]*n

    for i in range(n):
        for j in range(i):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(longest_increasing_subsequence([10,9,2,5,3,7,101,18]))




# def longest_increasing_subsequence_using_binary_search(nums):
#     n = len(nums)
#     sub = [0]

#     for num in nums:
#         if num > sub[-1]:
#             sub.append(num)
#         else:
#             sub.sort()
#             sub[0] = num
#     return sub
# print(longest_increasing_subsequence_using_binary_search([10,9,2,5,3,7,101,18]))
# # def smallest_no_greater_than_num(sub, num):
# #     left, right = 0, len(sub)


# def longest_increasing_subsequence(nums):
#     n = len(nums)
#     dp = []

#     for i in range(n):
#         for j in range(i):
#             if nums[i] < nums[j]:
#                 dp.append(nums[j])
#     return max(dp)

# print(longest_increasing_subsequence([10,9,2,5,3,7,101,18]))

