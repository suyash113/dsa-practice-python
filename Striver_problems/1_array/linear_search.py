class Solution:
    def linearSearch(self, nums, target):
        for i in nums:
            if i == target:
                return nums.index(i)
        return -1
print(Solution().linearSearch([2, 3, 4, 5, 3], 3))