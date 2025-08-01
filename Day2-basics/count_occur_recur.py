def count_occurrences(arr, target,i=0):
    if i >=len(arr):
        return 0 
    count = 1 if arr[i] == target else 0
    return count + count_occurrences(arr, target, i + 1)
# print(count_occurrences([6, 3, 6, 1, 6], 6))

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)
print(power(2,5))