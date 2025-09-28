class Solution:
    def mostFrequentElement(self, nums):
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] = count.get(i, 0) + 1
                all_keys = [key for key, val in count.items() if val == max(count.values())]
        return all_keys[0]

print(Solution().mostFrequentElement([4, 4, 5, 5, 6]))