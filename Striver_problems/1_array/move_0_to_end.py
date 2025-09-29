class Solution:
    def moveZeroes(self, nums):
        left = 0 
        right = 1
        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[right],nums[left] = nums[left], nums[right]
                left += 1
            right += 1
        return nums
print(Solution().moveZeroes([0, 1, 4, 0, 5, 2]))
