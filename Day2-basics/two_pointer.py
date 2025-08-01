def reverse_list(l):
    left = 0
    right = len(l)-1
    while left < right:
        l[left], l[right] = l[right], l[left]
        left +=1
        right -=1
    return l

# print(reverse_list([1,2,3,4,5]))

def find_max_min(l):
    min = l[0]
    max = l[0]
    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

# print(find_max_min([1,2,3,4,5]))

def move_zeros(arr):
    left = 0
    for right in range(len(arr)) :
        if arr[right] != 0:
            arr[right], arr[left] = arr[left],arr[right]
            left += 1
    return arr
# print(move_zeros([0, 1, 0, 3, 12,0,23,78,34]))

# def two_sum(arr, target):
#     indexes = []
#     left = 0
#     right = 1
#     while left < len(arr)-1:
#         if arr[left] + arr[right] == target:
#             indexes.append((left,right))
#         right += 1
#         if right > len(arr) -1:
#             left += 1
#             right = left +1
            
        
#     return indexes
def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
print(two_sum([2, 7, 11, 15], 9))
        
