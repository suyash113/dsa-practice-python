class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            i += 1
        return len(nums)
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

#  i, j = 0, 1
#         while j <= len(nums):
#             if nums[i] == nums[j]:
#                 nums.pop(j)
#                 j += 1
#             else:
#                 i += 1
#         return nums
