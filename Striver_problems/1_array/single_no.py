class Solution:
    def singleNumber(self, nums):
        #your code goes here
        count ={}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i, j in count.items():
            if j == 1:
                return i 
print(Solution().singleNumber([1, 2, 2, 4, 3, 1, 4]))