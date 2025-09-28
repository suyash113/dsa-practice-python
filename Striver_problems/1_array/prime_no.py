class Solution:
    def isPrime(self, n):
        #your code goes here
        for i in range(2, n//2):
            if n % i == 0:
                return False
        return True
print(Solution().isPrime(5))