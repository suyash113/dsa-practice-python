class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if n == 0:
            return 
        self.printNumbers(n-1)
        print(n)
print(Solution().printNumbers(5))

# def print_numbers(n):
#     if n == 0:
#         return
#     print_numbers(n - 1)
#     print(n)

# # Example usage
# print_numbers(6)