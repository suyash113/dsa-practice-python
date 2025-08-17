def linear_searching(arr, target):
    max_value = arr[0]
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    

            