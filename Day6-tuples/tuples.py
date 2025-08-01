def sum_product(input_tuple):
    sum1 = 0
    prod1 = 1
    for i in input_tuple:
        sum1 += i
        prod1 *= i 
    return sum1, prod1
# print(sum_product((1,2,3,4)))

def tuple_elementwise_sum(tuple1, tuple2):
    # result = []
    # for i in range(len(tuple1)):
    #     result.append(tuple1[i] + tuple2[i])
    # return tuple(result)
    return tuple(a + b for a, b in zip(tuple1, tuple2))
# print(tuple_elementwise_sum((1, 2, 3), (4, 5, 6)))

def insert_value_front(input_tuple, value_to_insert):
    # l1 = list(input_tuple)
    # l1.insert(0, value_to_insert)
    # return tuple(l1)
    return (value_to_insert,) + input_tuple
# print(insert_value_front((2, 3, 4),1))

def concatenate_strings(input_tuple):
    return " ".join(input_tuple)
# print(concatenate_strings(('Hello', 'World', 'from', 'Python')))

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))
# print(get_diagonal((
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
# )))

def common_elements(tuple1, tuple2):
    # return tuple(i for i in tuple1 if i in tuple2)
    return tuple(set(tuple1) & set(tuple2))
# print(common_elements((1, 2, 3, 4, 5), (4, 5, 6, 7, 8)))

