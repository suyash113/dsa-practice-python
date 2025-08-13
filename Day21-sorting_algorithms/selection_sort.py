def selection_sort(arr):
    count = 0
    n =len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                count += 1
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr, count

arr = [1,5,3,6,2]
print(selection_sort(arr))