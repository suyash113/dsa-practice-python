class Solution:
    def secondLargestElement(self, nums):
        largest = 0
        secLargest = 0
        for i in nums:
            if i > largest:
                largest = i
        for i in nums:
            if i != largest and i > secLargest:
                secLargest = i
        if secLargest != 0 and largest != secLargest:
            return secLargest
        else:
            return -1
print(Solution().secondLargestElement([8, 8, 8]))