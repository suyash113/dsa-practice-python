def rotate_list(l,k):
    # a = l[:k]
    # l[:k] = l[-k:]
    # l[-k:] = a
    # return l
    return l[k:] + l[:k]
# arr = [1,2,3,4,5]
# k = 2
# print(rotate_list(arr,k))

def rm_spaces(l):
    # s1 = "".join(l.split())
    s1 = l.replace(" ", "")
    return s1 

# r = rm_spaces("Hello world!")
# print(r)



