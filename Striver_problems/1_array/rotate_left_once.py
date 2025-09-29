class Solution:
    def rotateArrayByOne(self, nums):
        rotated = nums[1:]
        rotated.append(nums[0])
        return rotated
print(Solution().rotateArrayByOne([-1, 0, 3, 6]))