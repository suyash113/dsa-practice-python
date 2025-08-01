def build_word_counts(text):
    l = text.split(" ")
    dict1 = {}
    for i in l:
        dict1[i] = dict1.get(i,0) + 1
    return max(list(dict1.values()))
# print(build_word_counts("the cat in the hat"))

def two_sum(nums, target): # leetcode 1
    seen_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen_map:
            return [seen_map[complement], i]
        seen_map[num] = i
# print(two_sum([ 11,2, 15,7],9))

def  word_count(text1): # leetcode 192
    list1 = text1.split()
    dict1= {}
    for i in list1:
        dict1[i] = dict1.get(i, 0) + 1 # the day is sunny the the the sunny is is
    sorted_dict = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
    return sorted_dict
# print(word_count("the day is sunny the the the sunny is is"))

def merge_dict(d1, d2):
    # d3 = {}
    # for i in d1.keys() or d2.keys():
    #     if i in d2.keys() and d1.keys():
    #         d3[i] = d1[i] + d2[i]
    #     elif i in d1.keys():
    #         d3[i] = d1[i]
    #     else:
    #         d3[i] = d2[i]    
    # return d3
    result = d1.copy()
    for key, value in d2.items():
        result[key] = result.get(key, 0) + value 
    return result
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
# print(merge_dict(dict1, dict2))

def max_value_key(my_dict):
    # max1 = 0
    # for i in my_dict.keys():
    #     if my_dict[i] > max1:
    #         max1 = my_dict[i]
    #     if i 
    # return [key for key, v in my_dict.items() if v == max1]
    return max(my_dict, key=my_dict.get)
# print(max_value_key({'a': 5, 'b': 9, 'c': 2}))

def reverse_dict(my_dict):
    reverse_dict = {}
    for key, value in my_dict.items():
        reverse_dict[value] = key
    return reverse_dict
    return {v:k for k, v in my_dict.items()}
# print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))

 

def filter_dict(my_dict, condition):
    # condition  = my_dict, lambda k, v: v % 2 == 0
    return {k: v for k, v in my_dict.items() if condition(k, v)}

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
# filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
# print(filtered_dict)

def check_same_frequency(list1, list2):
    freq1 = {}
    freq2 = {}
    for i in list1:
        freq1[i] = freq1.get(i, 0) + 1
    for i in list2:
        freq2[i] = freq2.get(i, 0) + 1
    return freq1 == freq2
# print(check_same_frequency([1, 2, 3, 2, 1], [3, 1, 2, 1, 3]))

