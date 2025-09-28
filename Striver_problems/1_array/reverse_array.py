class Solution:
    def reverse(self, arr: list, n: int) -> None:
        return arr[-1::-1]
print(Solution().reverse([1,2,3,4,5],5))