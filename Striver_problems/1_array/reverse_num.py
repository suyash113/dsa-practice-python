class Solution:
    def reverseNumber(self, n):
        num = 0
        while n > 0:
            digit = n % 10
            num = num*10 + digit
            n = n // 10
        return num
print(Solution().reverseNumber(144))