class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        return s == s[::-1]
print(Solution().palindromeCheck("hannah"))