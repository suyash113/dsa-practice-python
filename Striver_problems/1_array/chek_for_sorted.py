class Solution:
    def isSorted(self, nums):
        #your code goes here
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                pass
            else:
                return False
        return True
print(Solution().isSorted([1, 2, 1, 4, 5]))