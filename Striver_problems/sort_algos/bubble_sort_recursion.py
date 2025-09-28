class Solution:
    def bubbleSort(self, nums, n=None):
        if n == None:
            n = len(nums)
        if n == 1:
            return
        for i in range(n-1):
            if nums[i] > nums[i+1]:
               nums[i], nums[i+1] = nums[i+1], nums[i]
        self.bubbleSort(nums, n-1)

arr = [64, 34, 25, 12, 22, 11, 90]
Solution().bubbleSort(arr)
print("Sorted array:", arr)
