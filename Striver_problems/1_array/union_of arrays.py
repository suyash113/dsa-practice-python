# class Solution:
#     def unionArray(self, nums1, nums2):
#         for i in range(len(nums2)):
#             for j in range(i,len(nums1)):
#                 if nums1[-1] < nums2[i]:
#                     nums1.append(nums2[i])  
#                 elif nums2[i] > nums1[j]:
#                     nums1.insert(j, nums2[i])
                                  
#         return nums1
# print(Solution().unionArray([1, 2, 3, 4, 5], [1, 2, 7]))

class Solution:
    def unionArray(self, nums1, nums2):
        i, j = 0, 0
        union = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                if not union or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                if not union or union[-1] != nums2[j]:
                    union.append(nums2[j])
                j += 1
            else:
                if not union or union[-1] != nums1[i]:
                    union.append(nums1[i])
                i += 1
                j += 1

        while i < len(nums1):
            if not union or union[-1] != nums1[i]:
                union.append(nums1[i])
            i += 1

        while j < len(nums2):
            if not union or union[-1] != nums2[j]:
                union.append(nums2[j])
            j += 1

        return union
print(Solution().unionArray([1, 2, 3, 4, 5], [1, 2, 7]))