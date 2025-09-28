class Solution:
    def isPalindrome(self, n):
        reversed_num = 0
        num = n
        while n > 0:
            digit  = n % 10
            reversed_num = reversed_num*10 + digit
            n = n // 10
        if reversed_num == num:
            return True
        else:
            return False
print(Solution().isPalindrome(122))