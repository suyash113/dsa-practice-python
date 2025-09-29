class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        s1 = ''.join(char.lower() for char in s if char.isalnum())
        print(s1)
        return s1 == s1[::-1]
print(Solution().palindromeCheck("A man, a plan, a canal: Panama"))