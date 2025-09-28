def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_num = i
        for j in range(n):
            if nums[min_num] < nums[j]:
                min_num = j
                nums[min_num], nums[i] = nums[i], nums[min_num]
    return nums
print(selection_sort([4,5,2,3,9,1]))