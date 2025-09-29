class Solution:
    def rotateArray(self, nums, k):
        if k > len(nums):
            k = k - len(nums)
        rotated = nums[k:]
        for i in nums[:k]:
            rotated.append(i)
        return rotated
print(Solution().rotateArray( [3, 4, 1, 5, 3, -5],8))