def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        mid = (left + right)//2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [2, 3, 4, 5, 8]
print("Binary Search 4:", binary_search(nums, 2))  # 2
print("Binary Search 10:", binary_search(nums, 10)) # -1