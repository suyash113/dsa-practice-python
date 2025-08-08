
    
# def heapify(arr, n, i):
#     biggest = i
#     left = 2*i + 1
#     right = 2*i + 2

#     if left < n and arr[left] > arr[biggest]:
#         biggest = left
#     if right < n and arr[right] > arr[biggest]:
#         biggest = right
    
#     if i != biggest:
#         arr[i], arr[biggest] = arr[biggest], arr[i]
#         i = biggest
#     else:
#         return None
#     heapify(arr, n, i)

# def heap_sort(arr):
#     n = len(arr)

#     for i in range(n//2-1, -1, -1):
#         heapify(arr, n, i)
    
#     for i in range(n-1, 0, -1):
#         arr[0], arr[i] = arr[i], arr[0]
#         heapify(arr, i, 0)

# arr = [5,3,8,4,1,2]
# print("Original:", arr)

# heap_sort(arr)

# print("Sorted:", arr)


















def heapify(arr, n, i):
    biggest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[biggest] < arr[left]:
        biggest = left
    if right < n and arr[biggest] < arr[right]:
        biggest = right
    
    if i != biggest:
        arr[biggest], arr[i] = arr[i], arr[biggest]
        i = biggest
    else:
        return None
    heapify(arr, n, i)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

arr = [5,3,8,4,1,2]
print("Original:", arr)

heap_sort(arr)

print("Sorted:", arr)