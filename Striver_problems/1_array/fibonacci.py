class Solution:
    def countFrequencies(self, nums: list) -> list:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        return [[key, value] for key, value in freq_map.items()]

# Example usage
nums = [1, 2, 2, 1, 3]
print(Solution().countFrequencies(nums))
