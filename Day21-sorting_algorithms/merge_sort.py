def merge_sort(arr1):
    if len(arr1) <= 1:
        return arr1
    
    mid = len(arr1)//2
    left = merge_sort(arr1[:mid])
    right = merge_sort(arr1[mid:])
    
    return merge(left, right)

def merge(left, right):
    i = 0
    j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

nums = [5, 3, 8, 4, 2]
print("Original:", nums)
print("Sorted:", merge_sort(nums)) 