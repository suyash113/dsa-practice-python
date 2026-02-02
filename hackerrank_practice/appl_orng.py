def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    appl_count = 0
    orng_count =  0
    for i in range(len(apples)):
        if s <= a + apples[i] <= t :
            appl_count += 1
    for i in range(len(oranges)):
        if s <= b + oranges[i] <= t:
            orng_count += 1
    print(appl_count)
    print(orng_count)

s, t, a, b, n1, n2, apples, oranges = 7, 11, 5, 15, 3, 2,[-2, 2, 1], [5, -6] #2, 3, 1, 5, 1, 1, [2], [-2] # 
countApplesAndOranges(s, t, a, b, apples, oranges)