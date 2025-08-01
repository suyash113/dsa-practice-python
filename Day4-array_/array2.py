def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    
    prefix_product = 1
    for i in range(n):
        answer[i] = prefix_product
        prefix_product *= nums[i]
        

    postfix_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= postfix_product
        postfix_product *= nums[i]
        
    return answer


print(product_except_self([1, 2, 3, 4]))
# Output: [24, 12, 8, 6]


# LeetCode #42

# def trap(heights):
    # traped = 0
    # j = 1
    # for i in range(len(heights)-1):
    #     j = heights.index(heights[i] if heights[i] > )
    #     trap = (heights[i] - heights[j])
            