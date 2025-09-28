class Solution:
    def insertionSort(self, nums, i=None):
        if i == None:
            i = 1
        if i == len(nums):
            return nums
        key = nums[i]
        j = i-1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
        return self.insertionSort(nums, i+1)
print(Solution().insertionSort([4,5,2,3,9,1]))