class Solution:
    def countDigit(self, n):
        count = 0
        while n > 0:
            n = n // 10
            count += 1
        return count

print(Solution().countDigit(144))