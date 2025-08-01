def double_list(l):
    return l
# print(double_list([1,2,3]))

def array_sum(arr, i=0):
    if i == len(arr):
        return 0
    return arr[i] + array_sum(arr, i+1)

# arr = [1,2,3,4]
# print(array_sum(arr))

def reverse_string(s):
    if len(s)<= 1:
        return s
    return reverse_string(s[1:])+ s[0]

# s = 'hello'
# print(reverse_string(s))

def count_occur(arr, target, i = 0):
    if arr[0] == target:
        i +=1
    if len(arr) <= 1:
        return i
    return count_occur(arr[1:], target, i)

arr = [6,3,6,1,6]
result = count_occur(arr, 6)
print(result)