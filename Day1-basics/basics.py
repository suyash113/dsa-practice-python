arr = [1,2,3,4,5]
arr.append(6)
arr[0] = 10
# print(arr)

def is_even(n):
    if n % 2 == 0 and n != 0:
        print(n, "is even")
    else:
        print(n, "is not even")
# is_even(8)

def sum_list(l):
    sum = 0
    for i in l:
        sum = sum + i
    print("sum is",sum)

l1 = [2,4,6,5,7]
# sum_list(l1)

def max_of_three(n1, n2, n3):
    gr = n1
    if n2 > gr:
        gr = n2 
    if n3 > gr:
        gr = n3
    print('Greatest no of three is', gr)

# print(max(5,5,3))
max_of_three(5,7,3)