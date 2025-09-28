class Solution:
    def isArmstrong(self, n):
        count = 0
        num = n
        while num > 0:
            num = num // 10
            count += 1
        num2 = n
        am_num = 0
        for i in range(count):
            digit = num2 % 10
            am_num += digit**count
            num2 = num2 // 10
        return am_num == n

print(Solution().isArmstrong(153))