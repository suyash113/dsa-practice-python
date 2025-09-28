class Solution: 
    def GCD(self, n1, n2):
        gcd = 0
        for i in range(1, n2+1):
            if n1%i == 0 and n2%i == 0:
                gcd = i
        return gcd
print(Solution().GCD(8,6))