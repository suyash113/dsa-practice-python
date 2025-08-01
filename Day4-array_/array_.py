def sum_even_indexed(nums):
    sum = 0
    for i in range(len(nums)):
        if i%2 == 0:
            sum = sum + nums[i] 
    return sum 
# print(sum_even_indexed([10, 20, 30, 40, 50]))

def find_min(nums):
    min = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < min:
            min  = nums[i]
    return min 
# print(find_min([5,2,3,1,6,19]))

def count_positive(nums):
    count = 0
    for i in nums:
        if i > 0:
            count += 1
    return count 
# print(count_positive([-1,4,5,6,-3,1,-4,-6,0]))

def make_squares(n):
    squares = []
    for i in range(1, n+1):
        squares.append(i**2)
    return squares
# print(make_squares(5))

def contains_element(elements, target):
    if target in elements:
        return True
    else:
        return False
# print(contains_element([2,5,6,1,99,0,33], 33))

def reverse_list(items):
    for i in range(0, (len(items)//2)):
        items[i], items[len(items)-1-i] = items[len(items)-1-i], items[i]
        items
    return items
# print(reverse_list([1,2,3,4,5,6]))



#mideum level difficulty from here ----------------

def rotate_left(nums, k): 
    # for i in range(k):
    #     nums.append(nums[0])
    #     nums.pop(0)
    # return nums 
    return nums[k:] + nums[:k]
# print(rotate_left([1,2,3,4,5],2))

def find_missing(nums):
    n = []
    # for i in range(len(nums)-1):
    #     if nums[i+1] - nums[i] != 1:
    #         n.append((nums[i+1] + nums[i])//2)
    # return n 
    for i in range(1,max(nums)):
        if i not in set(nums):
            n.append(i)
    return n
# print(find_missing([1,2,4,6,7]))

def remove_duplicates(sorted_nums):
    # n = len(sorted_nums)
    # i=1
    # while i < n:
    #     if sorted_nums[i] != sorted_nums[i-1]:
    #         i +=1
    #     else:
    #         sorted_nums.pop(i)
    #         n -=1
    # return n
    write_index = 1
    for i in range(1, len(sorted_nums)):
        if sorted_nums[i] != sorted_nums[i-1]:
            sorted_nums[write_index] = sorted_nums[i]
            write_index +=1
    return write_index
# print(remove_duplicates([0,0,1,1,1,1,2,2]))

def second_largest(nums):
    # nums.sort()
    # return nums[-2]
    max1 = nums[0]
    max2 = nums[1]
    for i in nums:
        if i > max2 and max2 < max1:
            max2 = i
        if i > max1:
            max1 = i    
    return max2
# print(second_largest([1,2,3,4,51,11,43,89]))

def running_sums(nums):
    all_sums = []
    running_sum = 0
    for i in range(1,len(nums)+1):
        running_sum += i 
        all_sums.append(running_sum)
    return all_sums
# print(running_sums([1,2,3,4]))