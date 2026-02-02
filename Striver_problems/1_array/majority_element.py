class Solution:
    def majorityElement(self, nums):
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i in count:
            if count[i] > len(nums)//2:
                return i


print(Solution().majorityElement([1, 1, 1, 2, 1, 2]))