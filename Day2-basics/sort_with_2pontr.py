def remove_duplicates(arr):
    write_pos = 1 
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[write_pos] = arr[i]
            write_pos +=1
    return write_pos
# print(remove_duplicates([1, 1, 2, 2, 3]))            
            
def merge_sorted_arrays(arr1,arr2):
    i,j = 0,0
    result = []
    while i in range(len(arr1)) and j in range(len(arr2)):
        if arr1[i]<=arr2[j]:
            result.append(arr1[i])
            i +=1
        else:
            result.append(arr2[j])
            j +=1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
# print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False 
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j] 
                swapped = True
        if not swapped:
            return arr
print(bubble_sort([64, 34, 25, 12, 22]))