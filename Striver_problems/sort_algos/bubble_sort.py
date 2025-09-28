def buuble_sort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] < nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
print(buuble_sort([4,5,2,3,9,1]))