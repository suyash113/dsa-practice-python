class Solution:
    def missingNumber(self, nums):
        sum1 = 0
        total = sum(range(1, max(nums) + 1))
        for i in nums:
            sum1 += i
        return total - sum1 
print(Solution().missingNumber([0, 1, 2, 4, 5, 6]))