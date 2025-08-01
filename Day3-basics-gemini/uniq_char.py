def find_first_unique(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c,0) + 1
    for i, c in enumerate(s):
        if freq[c] == 1:
            return i 
    return -1

# print(find_first_unique("loveleetcode"))      

def count_chars(s):
    count = {}
    if s == "":
        return 0
    for i in s:
        count[i] = count.get(i,0) + 1
    return count

# print(count_chars("hello"))

def count_occur(arr, tar, i = 0):
    if i >= len(arr):
        return 0
    count = 1 if arr[i] == tar else 0
    return count + count_occur(arr, tar,i+1)
print(count_occur([1,2,3,4,3,2,1,3],3))