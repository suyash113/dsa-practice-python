def insertion_sort(arr):
    n = len(arr)
    count = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            count += 1
            j -= 1
        arr[j+1] = key
    return arr, count

arr = [1,5,3,6,2]
print(insertion_sort(arr))




# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and arr[j] > key:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr

# arr = [1,5,3,6,2]
# print(insertion_sort(arr))