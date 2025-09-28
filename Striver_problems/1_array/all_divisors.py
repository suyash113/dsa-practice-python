class Solution:
    def divisors(self, n):
        return [i for i in range(1, n+1) if n % i == 0]
print(Solution().divisors(6))