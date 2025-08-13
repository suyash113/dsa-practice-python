# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#                 swapped = True
#         if not swapped:
#             break
#     return arr

# arr = [1,2, 4,6,3,5,0]
# print(bubble_sort(arr))



def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
                count += 1
        if not swapped:
            break
    return arr, count

arr = [1,5,3,6,2]
print(bubble_sort(arr))