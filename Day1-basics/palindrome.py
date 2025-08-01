def is_palindrome(s):
    l = ''
    s1 = ''.join(char.lower() for char in s if char.isalnum())
    # s1 = clean_text.lower()
    # for i in range(len(s1)-1, -1, -1):
    #     l = l + s1[i]
    if s1 == s1[::-1]:
        return True
    # if s1 == l:
    #     return True 
    else:
        return False 

result = is_palindrome("A man, a plan, a canal:Panama")
print(result) # A man, a plan, a canal:Panama

def sum_even_no(arr):
    sum = 0
    for i in arr:
        if i % 2 == 0:
            sum = sum + i 
    return sum 
# result = sum_even_no([1,2,3,4,5,6])
# print(result)

def reverse_list(arr):
    l = []
    for i in range(len(arr)- 1, -1, -1):
        l.append(arr[i])
    return l 

# result = reverse_list([1,2,3,4])
# print(result)