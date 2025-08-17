# def bubble_up(arr, n, i):
#     biggest = i
#     left = 2*i +1
#     right = 2*i +2
    
#     if left < n and arr[left] > arr[biggest]:
#         biggest = left
#     if right < n and arr[right] > arr[biggest]:
#         biggest = right
    
#     if i != biggest:
#         arr[i], arr[biggest] = arr[biggest], arr[i]
#         i = biggest
#     else:
#         return None
#     bubble_up(arr, n, i)

    
# def heap_sort(arr):
#     n = len(arr)
    
#     for i in range(n//2 -1, -1,-1):
#         bubble_up(arr, n, i)
    
#     for i in range(n-1, 0,-1):
#         arr[i], arr[0] = arr[0], arr[i]
#         bubble_up(arr, i, 0)
        
#     return arr

# nums = [5, 3, 8, 4, 2]
# print("Original:", nums)
# print("Sorted:", heap_sort(nums))



def bubble_up(arr, n, i):
    biggest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[biggest]:
        biggest = left
    if right < n and arr[right] > arr[biggest]:
        biggest = right
    
    
    if i != biggest:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        i = biggest
    else:
        return None
    bubble_up(arr, n, i)
    
def heap_sort(arr):
    n = len(arr)
    
    for i in range(n//2-1,-1,-1):
        bubble_up(arr, n, i)
    
    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        bubble_up(arr,i,0)
    return arr

nums = [5, 3, 8, 4, 2]
print("Original:", nums)
print("Sorted:", heap_sort(nums))
