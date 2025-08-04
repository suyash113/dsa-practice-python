def reverse_string(str1):
    stack = []
    for char in str1:
        stack.append(char)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

input_str = "hello"
print(reverse_string(input_str))