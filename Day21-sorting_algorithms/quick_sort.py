# def quick_sort(arr): not in place
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr)//2]
    
#     left = [x for x in arr if x < pivot]
#     mid  = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
    
#     return quick_sort(left) + mid + quick_sort(right)

# nums = [5, 3, 8, 4, 2]
# print("Original:", nums)
# print("Sorted:", quick_sort(nums)) 


# in place quick sort
# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi-1)
#         quick_sort(arr, pi+1, high)
    
# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
    
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
            
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i+1

# nums = [5, 3, 8, 4, 2]
# print("Original:", nums)
# quick_sort(nums, 0, len(nums)-1)
# print("Sorted:", nums) 





def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

nums = [5, 3, 8, 4, 2]
print("Original:", nums)
quick_sort(nums, 0, len(nums)-1)
print("Sorted:", nums) 