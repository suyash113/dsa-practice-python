class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        duplicate = []
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            i += 1
        return nums
print(Solution().removeDuplicates([0, 0, 3, 3, 5, 6,6]))

# while i > len(nums):
