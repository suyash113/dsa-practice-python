def kangaroo(x1, v1, x2, v2):
    # Write your code here
    j = (x2 -x1)%(v1 - v2)
    print(j)
    print(j == 0)
x1, v1, x2, v2 = 43, 2, 70, 2#0, 3, 4, 2
kangaroo(x1, v1, x2, v2)